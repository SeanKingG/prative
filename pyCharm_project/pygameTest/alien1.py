import sys
import pygame
from settings import settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('alien invasion')
    ship = Ship(screen)



    while True:
        gf.check_event(ship)
        ship.update()

        gf.update_screen(ai_settings, screen, ship)

run_game()