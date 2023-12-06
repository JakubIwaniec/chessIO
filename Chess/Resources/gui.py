"""
24/11
Skrpt opisuje i tworzy wszystkie obiekty
związane z GUI
"""

import pygame
import pygame_menu
from typing import Optional

import Chess.main
import Chess.Piece

# --- STAłE ---
# stałe Menus
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 800
MAIN_MENU_WIDTH = 400
MAIN_MENU_HEIGHT = 600
AUTHORS = 'Made by:\n'\
        'Jakub Iwaniec\n' \
        'Mikołaj Dettlaff\n' \
        'Miłosz Gostyński'
# stałe GameEngine
BOARD_WIDTH = 1000
BOARD_HEIGHT = 1000
BOARD_SQUARE_FIRST = (69, 69)
BOARD_SQUARE_SIZE = (107, 107)
BOARD_SQUARE_SPACING_PIXELS = 1
REFRESH_RATE = 60
# ---       ---


class Menus:
    # tworzenie wszystkich obiektów wszystkich menu
    def __init__(self):
        Menus._assert_constants_test()
        self._beatbox_gui = pygame_menu.Sound()
        self._beatbox_gui.load_example_sounds()

        self.menu = pygame_menu.Menu(
            title="Chess Game", width=MAIN_MENU_WIDTH, height=MAIN_MENU_HEIGHT, theme=pygame_menu.themes.THEME_DEFAULT)

        self.submenu_play = pygame_menu.Menu(
            title="Game Settings", width=self.menu.get_width(), height=self.menu.get_height())
        self.submenu_help = pygame_menu.Menu(
            title="About Chess", width=self.menu.get_width(), height=self.menu.get_height())
        self.submenu_authors = pygame_menu.Menu(
            title="Authors", width=self.menu.get_width(), height=self.menu.get_height()/2)

        Menus._add_properties_menu(self)
        Menus._add_properties_submenu_play(self)
        Menus._add_properties_submenu_help(self)
        Menus._add_properties_submenu_authors(self)
        Menus._add_properties_sounds(self)

    # testy defensywne stałych
    @staticmethod
    def _assert_constants_test() -> None:
        assert type(MAIN_MENU_WIDTH) is int
        assert type(MAIN_MENU_HEIGHT) is int
        assert WINDOW_WIDTH > MAIN_MENU_WIDTH
        assert WINDOW_HEIGHT > MAIN_MENU_HEIGHT

    # ----  nadanie atrybutów obiektom menu   ----
    @staticmethod
    def _add_properties_menu(self) -> None:
        self.menu.add.button(title="Play", action=self.submenu_play)
        self.menu.add.button(title="Guide to Chess", action=self.submenu_help)
        self.menu.add.button(title="Authors", action=self.submenu_authors)
        self.menu.add.button(title="Quit", action=pygame_menu.events.EXIT)

    @staticmethod
    def _add_properties_submenu_play(self) -> None:
        switch_ai = self.submenu_play.add.toggle_switch(
            title="Playmode",
            default=True,
            toggleswitch_id="switch_ai",
            state_text=('vs AI', 'vs Player'),
            state_text_font_size=18
        )
        self.selector_difficulty = self.submenu_play.add.dropselect(
            title="AI difficulty",
            items=[
                ("Novice", 0), ("Amateur", 1),
                ("Intermediate", 2), ("Pro", 3)],
            default=0,
            selection_box_width=173,
            selection_option_padding=(0, 5),
            selection_option_font_size=20
        )
        self.submenu_play.add.button(title="Begin game", action=GameEngine.run_game)

    @staticmethod
    def _add_properties_submenu_help(self) -> None:
        self.submenu_help.add.button(title="Chess Basics")
        self.submenu_help.add.button(title="Chess Openings")
        self.submenu_help.add.button(title="Advanced Topics")

    @staticmethod
    def _add_properties_submenu_authors(self) -> None:
        self.submenu_authors.add.label(AUTHORS, max_char=-1, font_size=20)

    # ---------------------------------------------

    # nadanie dźwięków obiektom menu (pygame_menu nie dzieli architektury z pygame) -
    #   - patrz: SoundEngine
    @staticmethod
    def _add_properties_sounds(self) -> None:
        self.menu.set_sound(self._beatbox_gui, recursive=True)
        self.submenu_play.set_sound(self._beatbox_gui, recursive=True)
        self.submenu_help.set_sound(self._beatbox_gui, recursive=True)
        self.submenu_authors.set_sound(self._beatbox_gui, recursive=True)


class BoardSquare(pygame.sprite.Sprite):
    def __init__(self, start_point: tuple = (0, 0)):
        super().__init__()
        self.start_point = start_point
        self.image = pygame.Surface(BOARD_SQUARE_SIZE, pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.marker_select = pygame.Color(0, 255, 0)
        self.marker_highlight = pygame.Color(0, 255, 0)
        self.is_selected: bool = False
        self.is_highlighted: bool = False

    def switch_select(self):
        color_mask = pygame.Surface(BOARD_SQUARE_SIZE)
        if self.is_selected:
            color_mask.fill(self.marker_select)
            color_mask.set_alpha(51)
            self.image.blit(color_mask, dest=(0, 0), special_flags=pygame.BLENDMODE_BLEND)
            self.is_selected = False
        else:
            self.is_selected = True

    def switch_highlight(self):
        color_mask = pygame.Surface(BOARD_SQUARE_SIZE)
        if self.is_highlighted:
            color_mask.fill(self.marker_highlight)
            color_mask.set_alpha(25)
            self.image.blit(color_mask, dest=(0, 0), special_flags=pygame.BLENDMODE_BLEND)
            self.is_highlighted = False
        else:
            self.is_highlighted = True

    def set_image(self, piece_element):
        if type(piece_element) is not str:
            print(type(piece_element))
            piece_element_image = pygame.image.load(piece_element.path_to_image).convert_alpha()
            piece_element_image = pygame.transform.scale(piece_element_image, BOARD_SQUARE_SIZE)
            self.image.blit(piece_element_image, (0, 0))
        else:
            transparent = pygame.Surface(BOARD_SQUARE_SIZE)
            transparent.fill((255, 255, 255))
            transparent.set_colorkey((255, 255, 255))
            self.image.blit(transparent, (0, 0))


class GameEngine:
    """
    Silnik gry - przechowuje/obsługuje obiekty graficzne,
    nanosi figury na planszę, ma metody statyczne
    do uruchamiania samej całej gry.
    """
    def __init__(self):
        self._window: Optional['pygame.Surface'] = None
        self._board_surface: Optional['pygame.Rect'] = None
        self._board_subsurfaces: Optional['tuple[pygame.Rect]'] = None
        self._board_image: Optional['str'] = None # dodaj set_engine_board_image
        # self._skin_pack: Optional['str'] = None # tutaj czy moze w pieces.py ???
        self._chessboard_state: Optional['list'] = None

        self.beatbox = SoundEngine()
        pygame.init()

    def set_engine_window(self, new_window: pygame.Surface):
        assert type(new_window) is pygame.Surface
        self._window = new_window

    def set_engine_board_surface(self, new_board_surface: pygame.Rect):
        assert type(new_board_surface) is pygame.Rect
        self._board_surface = new_board_surface

    def set_engine_board_subsurfaces(self, new_board_subsurfaces: list[pygame.Rect]):
        assert type(new_board_subsurfaces) is pygame.Rect
        self._board_surface = new_board_subsurfaces

    def set_engine_chessboard_state(self, new_chessboard_state):
        assert type(new_chessboard_state) is list and len(new_chessboard_state) == 8
        for row_index, row in enumerate(new_chessboard_state):
            assert len(new_chessboard_state[row_index]) == 8
        self._chessboard_state = new_chessboard_state

    @staticmethod
    def run_game():
        """
        print(chessboard.board[0]) # [r, n, b, q, k, b, n, r]
        print(chessboard.board[0][0]) # Rook
        print(type(chessboard.board[0][0])) # <class 'Chess.Piece.Rook'>
        print(repr(chessboard.board[0][0])) # r
        """
        chessboard = Chess.main.Chessboard()
        Chess.main.Chessboard.startgame(chessboard)
        print(chessboard.board)

        chessboard.print_board()
        window = pygame.display.set_mode(size=(BOARD_WIDTH, BOARD_HEIGHT))
        board_surface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        board_image = pygame.image.load("Images\\Chessboards\\Szachownica3.jpg")
        board_image = pygame.transform.scale(surface=board_image, size=(BOARD_WIDTH, BOARD_HEIGHT))

        board_surface.blit(source=board_image, dest=(0, 0))
        sprites = [
                [BoardSquare(start_point=(
                    column_index * (BOARD_SQUARE_SIZE[0] + BOARD_SQUARE_SPACING_PIXELS) + BOARD_SQUARE_FIRST[0],
                    row_index * (BOARD_SQUARE_SIZE[1] + BOARD_SQUARE_SPACING_PIXELS) + BOARD_SQUARE_FIRST[1]))
                 for column_index in range(8)] for row_index in range(8)
        ]

        for row_index, row in enumerate(sprites):
            for column_index, element in enumerate(sprites[row_index]):
                pass

        engine = GameEngine()
        engine.set_engine_window(window)
        engine.assign_board_state(chessboard.board, sprites, board_surface)

        pygame.display.flip()

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key is pygame.key.key_code('return'):
                        # test
                        sprites[0][0].switch_select()
                        print('Enter')
                    if event.key is pygame.key.key_code('backspace'):
                        # test
                        sprites[0][0].set_image(chessboard.board[0][0])
                        chessboard.move_piece(True, None, 1, 0, 3, 0)
                    if event.key is pygame.key.key_code('escape'):
                        engine.beatbox.play_click()
                        GameEngine.run_gui()
                    for row_index, row in enumerate(sprites):
                        for column_index, element in enumerate(sprites[row_index]):
                            if not element.is_selected:
                                element.set_image(chessboard.board[row_index][column_index])
                            board_surface.blit(sprites[row_index][column_index].image, sprites[row_index][column_index].start_point)

            window.blit(source=board_surface, dest=(0, 0))
            pygame.display.flip()

    @staticmethod
    def run_gui():
        # Podstawowa funkcja rysująca
        def update_background() -> None:

            bg_image.draw(surface=window)

        clock = pygame.time.Clock()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        bg_image = pygame_menu.BaseImage(image_path="Images/Backgrounds/main_menu2.jpg")
        # roboczy test, czy poprawnie załadowało plik .jpg
        print(bg_image.get_size())

        # Główna pętla menu
        while True:
            # Obsługa wejść od użytkownika
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
            # ...

            menu_interface = Menus()
            menu_interface.menu.mainloop(window, bgfun=update_background)
            pygame.display.flip()
            clock.tick(REFRESH_RATE)

    def assign_board_state(self, new_state: list, board_sprites: list[list[BoardSquare]], draw_on: pygame.Surface):
        """
        Ta funkcja ma drukować figury na planszy na podstawie stanu planszy
        ??? jak ma drukować wybraną figurę i sugerowane ruchy?
        :param new_state:
        :param board_sprites:
        :param draw_on:
        :return:
        """
        self.set_engine_chessboard_state(new_state)
        self.set_engine_window(draw_on)

        for row_index, row in enumerate(self._chessboard_state):
            for element_index, element in enumerate(self._chessboard_state[row_index]):
                print("(%i, %i)" % (row_index, element_index), end=' ')
                if str(element) == 'Pawn':
                    print("TO JEST PAWN -", end=' ')
                    if str(repr(element)) == 'p':
                        print("BIALY")
                    elif str(repr(element)) == 'P':
                        print("CZARNY")
                elif str(element) == 'Rook':
                    assert type(element) is Chess.Piece.Rook
                    print("TO JEST ROOK -", end=' ')
                    if str(repr(element)) == 'r':
                        print("BIALY")
                    elif str(repr(element)) == 'R':
                        print("CZARNY")
                elif str(element) == 'Knight':
                    print("TO JEST KNIGHT -", end=' ')
                    if str(repr(element)) == 'n':
                        print("BIALY")
                    elif str(repr(element)) == 'N':
                        print("CZARNY")
                elif str(element) == 'Bishop':
                    print("TO JEST BISHOP -", end=' ')
                    if str(repr(element)) == 'b':
                        print("BIALY")
                    elif str(repr(element)) == 'B':
                        print("CZARNY")
                elif str(element) == 'Queen':
                    print("TO JEST QUEEN -", end=' ')
                    if str(repr(element)) == 'q':
                        print("BIALY")
                    elif str(repr(element)) == 'Q':
                        print("CZARNY")
                elif str(element) == 'King':
                    print("TO JEST KING -", end=' ')
                    if str(repr(element)) == 'k':
                        print("BIALY")
                    elif str(repr(element)) == 'K':
                        print("CZARNY")
                else:
                    print("''")


class SoundEngine:
    """
    Silnik dźwiękowy (dla elementów z paczki pygame).
    """
    def __init__(self):
        pygame.mixer.init()
        self.click = pygame.mixer.Sound('Sounds/Klik.wav')
        self.volume = 0.7
    # do dokończenia ?

    def play_click(self):
        pygame.mixer.Sound.play(self.click)
        print("Playing sound!")


# przykładowe wywołanie obiektów w tym skrypcie
test = GameEngine()
test.run_gui()
