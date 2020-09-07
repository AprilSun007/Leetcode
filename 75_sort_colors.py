#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:11:24 2020

@author: jinwensun
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 这道题借鉴quick sort， 做法就是碰到0， 移到最前面， 碰到2 移到后面， i， j keep track on 下一个0 和1 应该移到的地方
        i = 0
        curr = 0
        j = len(nums) - 1
        
        while curr <= j:
            if nums[curr] == 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                i += 1
                curr += 1
                
            elif nums[curr] == 2:
                nums[j], nums[curr] = nums[curr], nums[j]
                j -= 1
                
            else:
                curr += 1
            
        
        