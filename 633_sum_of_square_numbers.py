#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:59:37 2020

@author: jinwensun
"""

from math import sqrt
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(sqrt(c)) + 1
        
        while(i <= j):
            if (i*i + j*j > c):
                j -= 1
            elif(i*i + j*j < c):
                i += 1
            else:
                return True
        return False
        
        