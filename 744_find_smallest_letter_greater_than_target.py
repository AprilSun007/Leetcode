#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:07:48 2020

@author: jinwensun
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[0] > target:
            return letters[0]
        elif letters[-1] <= target:
            return letters[0]
        
        i = 0
        j = len(letters) - 1
        
        while(i + 1 < j):
            mid = i + (j -i)//2
            if letters[mid] <= target:
                i = mid + 1
            else:
                j = mid
                
        if i < j:
            if letters[i] <= target:
                return letters[j]
            else:
                return letters[i]
        else:
            return letters[i]