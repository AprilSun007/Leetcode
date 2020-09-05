#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:47:10 2020

@author: jinwensun
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(nums):
            if nums[ptr1] != 0:
                #tmp = nums[ptr2]
                nums[ptr2] = nums[ptr1]
                #nums[ptr1] = tmp
            
                ptr2 = ptr2 + 1
                
            ptr1 = ptr1 + 1
        while ptr2 < len(nums):
            nums[ptr2] = 0
            ptr2 = ptr2 + 1
            
        return nums
        