'''
Author: taobo
Date: 2020-11-12 20:56:14
LastEditTime: 2020-11-13 12:06:24
'''
class GameStats(object):
  def __init__(self, ai_setting):
    self.ai_setting = ai_setting
    self.game_active = False
    self.reset_stats() 

  def reset_stats(self):
    self.ships_left = self.ai_setting.ships_limit
    self.score = 0