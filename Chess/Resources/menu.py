"""
13/11
Skrpt opisuje i tworzy wszystkie obiekty
związane z GUI
"""

import pygame
import pygame_menu


# Podstawowa funkcja rysująca
def update_background() -> None:

    bg_image.draw(surface=window)


# stałe
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_image = pygame_menu.BaseImage(image_path="main_menu2.jpg")
# roboczy test, czy poprawnie załadowało plik .jpg
print(bg_image.get_size())

# tworzenie menu
menu = pygame_menu.Menu(title="Chess Game", width=400, height=600,
                        theme=pygame_menu.themes.THEME_DEFAULT)
menu.add.button(title="Play")
menu.add.button(title="Quit", action=pygame_menu.events.EXIT)
menu.add.label("v 0.2").set_padding((50, 0, 0, 0))


# Główna pętla
while True:
    # Obsługa wejść od użytkownika
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            raise SystemExit

    # ...

    menu.mainloop(window, bgfun=update_background)
    menu.force_surface_update()
    # Odświeżanie
    clock.tick(60)      # (60 FPS)
