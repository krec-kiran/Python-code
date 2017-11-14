import sys
import pygame
from ship import Ship
import game_functions as gf


class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship

    ship = Ship(screen)

    while True:
        gf.check_events()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()
