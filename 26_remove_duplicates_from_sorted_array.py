#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:08:56 2020

@author: jinwensun
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums is None) or (len(nums) == 0):
            return -1
        
        ptr1 = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[ptr1]:
                continue
            else:
                ptr1 = ptr1 + 1
                nums[ptr1] = nums[i]
                    
        return ptr1 + 1
            