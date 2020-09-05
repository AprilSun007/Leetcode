#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:29:38 2020

@author: jinwensun
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :Time Complexity: O(n^2)
        :Space Complexity O(n)
        
        
        """
        if (nums is None) or (len(nums) == 0):
            return 0
        
        DP = [1]*len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    DP[i] = max(DP[i], DP[j]+1)
                    
        return max(DP)
        