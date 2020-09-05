#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:30:41 2020

@author: jinwensun
"""

from collections import defaultdict
class Leaderboard(object):

    def __init__(self):
        self.dict = defaultdict(int)
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.dict[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        return sum(sorted(self.dict.values(), reverse = True)[0:K])
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.dict[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)