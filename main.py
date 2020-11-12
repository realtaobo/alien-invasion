'''
Author: taobo
Date: 2020-11-11 19:33:13
LastEditTime: 2020-11-12 21:26:10
'''
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats


def run_game():
    pygame.init()
    pygame.display.set_caption('Alien Invasion')

    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))

    ship = Ship(screen, ai_setting)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_setting)

    gf.create_fleet(ai_setting, screen, aliens, ship)
    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, ai_setting, screen, aliens, ship)
            gf.update_aliens(ai_setting, stats, screen, aliens, ship, bullets)
        gf.update_screen(ai_setting, screen, ship, aliens, bullets)
        # 该break是为了 travis CI 可以正常结束，调试使用时须删除
        break

run_game()

