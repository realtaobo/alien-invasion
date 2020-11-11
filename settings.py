class Settings(object):
    """该类存储游戏所有的设置"""

    def __init__(self):
        self.screen_height = 1200
        self.screen_width = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 4
        # bullet setting
        self.bullet_speed_factor = 0.1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
