#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:31:49 2020

@author: jinwensun
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) == 0:
            return s
        
        i = 0
        j = len(s) - 1
        while(i < j):
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1