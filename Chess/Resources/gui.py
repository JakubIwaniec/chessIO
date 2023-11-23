"""
23/11
Skrpt opisuje i tworzy wszystkie obiekty
związane z GUI
"""

import pygame
import pygame_menu

# stałe
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
MAIN_MENU_WIDTH = 400
MAIN_MENU_HEIGHT = 600
REFRESH_RATE = 60
AUTHORS = 'Made by:\n'\
        'Jakub Iwaniec\n' \
        'Miłosz Gostyński\n' \
        'Mikołaj Dettlaff'


class Menus:
    # tworzenie wszystkich obiektów wszystkich menu
    def __init__(self):
        Menus._assert_constants_test()

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

    # testy defensywne stałych
    @staticmethod
    def _assert_constants_test():
        assert type(MAIN_MENU_WIDTH) is int
        assert type(MAIN_MENU_HEIGHT) is int
        assert WINDOW_WIDTH > MAIN_MENU_WIDTH
        assert WINDOW_HEIGHT > MAIN_MENU_HEIGHT

    @staticmethod
    def _add_properties_menu(self):
        self.menu.add.button(title="Play", action=self.submenu_play)
        self.menu.add.button(title="New To Chess?", action=self.submenu_help)
        self.menu.add.button(title="Authors", action=self.submenu_authors)
        self.menu.add.button(title="Quit", action=pygame_menu.events.EXIT)

    @staticmethod
    def _add_properties_submenu_play(self):
        self.submenu_play.add.button(title="Begin game", action=pygame_menu.events.CLOSE)

    @staticmethod
    def _add_properties_submenu_help(self) -> None:
        self.submenu_help.add.button(title="Help")

    @staticmethod
    def _add_properties_submenu_authors(self) -> None:
        self.submenu_authors.add.label(AUTHORS, max_char=-1, font_size=20)


class GameEngine:
    def __init__(self, window_surface: pygame.Surface):
        self.window_surface = window_surface


# Podstawowa funkcja rysująca
def update_background() -> None:

    bg_image.draw(surface=window)


pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_image = pygame_menu.BaseImage(image_path="main_menu2.jpg")
# roboczy test, czy poprawnie załadowało plik .jpg
print(bg_image.get_size())

# Główna pętla menu (tymczasowa)
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
