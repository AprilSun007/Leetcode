#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:29:29 2020

@author: jinwensun
"""

from collections import defaultdict 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_dict = defaultdict(int)
        for n in nums:
            number_dict[n] += 1
            
        for k in number_dict.keys():
            if number_dict[k] == 1:
                return k