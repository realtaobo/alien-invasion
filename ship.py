import pygame


class Ship(object):
    def __init__(self, screen, ai_setting):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.ai_setting = ai_setting

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.centerx > 0:
            self.center -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center
