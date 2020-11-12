'''
Author: taobo
Date: 2020-11-11 19:33:13
LastEditTime: 2020-11-12 21:25:27
'''
class Settings(object):
    """该类存储游戏所有的设置"""

    def __init__(self):
        self.screen_height = 600
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1
        # bullet setting
        self.bullet_speed_factor = 0.8
        self.bullet_width = 300
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100
        # alien setting
        self.alien_speed_factor = 0.7
        self.alien_drop_speed = 100
        self.fleet_direction = 1
        # ships
        self.ships_limit = 3
