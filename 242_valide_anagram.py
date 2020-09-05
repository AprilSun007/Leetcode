#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:26:49 2020

@author: jinwensun
"""

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # time complexity O(n)
        # if u do sort time complexity O(nlogn)
        return Counter(s) == Counter(t)