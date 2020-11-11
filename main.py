'''
Author: taobo
Date: 2020-11-11 19:33:13
LastEditTime: 2020-11-11 21:19:17
'''
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    pygame.display.set_caption('Alien Invasion')

    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_height, ai_setting.screen_width))

    ship = Ship(screen, ai_setting)
    bullets = Group()

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, bullets)


run_game()

