#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:34:23 2020

@author: jinwensun
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums is None) or (len(nums) == 0):
            return None
        
        strt = 0
        end = len(nums) -1
        
        while(strt + 1 < end):
            mid = strt + (end - strt)//2
            
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif (nums[strt] < nums[mid]) & (nums[mid] < nums[end]):
                return nums[strt]
            elif nums[strt] > nums[mid]:
                end = mid
            else:
                strt = mid
                
        
        if nums[strt] < nums[end]:
            return nums[strt]
        else:
            return nums[end]