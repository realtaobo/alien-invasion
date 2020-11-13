'''
Author: taobo
Date: 2020-11-13 12:00:55
LastEditTime: 2020-11-13 12:10:41
'''
import pygame.font


class Scoreboard(object):
  """
  显示得分消息的类
  """
  def __init__(self, ai_setting, screen, stats):
    self.ai_setting = ai_setting
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.stats = stats
    # font
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)
    # prepare score image
    self.prep_score()

  def prep_score(self):
    rounded_score = round(self.stats.score, -1)
    score_str = "{:,}".format(rounded_score)
    self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def show_score(self):
    self.screen.blit(self.score_image, self.score_rect)