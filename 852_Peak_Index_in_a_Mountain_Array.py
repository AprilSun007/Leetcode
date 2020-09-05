#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:45:05 2020

@author: jinwensun
"""

class Solution(object):
    def peakIndexInMountainArray(self, nums):
        """
        :type A: List[int]
        :rtype: int
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        if (nums is None) or (len(nums) == 0):
            return -1
        
        strt = 0
        end = len(nums) - 1
        
        while(strt + 1 < end):
            mid = strt + (end - strt) //2
            
            if (nums[mid] > nums[mid-1]) & (nums[mid] > nums[mid+1]):
                return mid
            elif (nums[mid] > nums[mid-1]) & (nums[mid] < nums[mid+1]):
                strt = mid
            else:
                end = mid
                
        if nums[strt] > nums[end]:
            return strt
        else:
            return end