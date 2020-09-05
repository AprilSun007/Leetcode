#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:38:19 2020

@author: jinwensun
"""

class Solution(object):
    def square_sum(self, n):
        n_str = str(n)
        n_sum = 0
        for char in n_str:
            n_sum += int(char)*int(char)
        return n_sum
            
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        computed = set()
        
        while True:
            n_sum = self.square_sum(n)
            if n_sum == 1:
                return True
            if n_sum in computed:
                return False
            computed.add(n)
            n = n_sum