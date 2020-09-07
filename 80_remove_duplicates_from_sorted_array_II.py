#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:43:42 2020

@author: jinwensun
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        cnt = 1
        
        while (j < len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
                j += 1
                cnt = 1
            else:
                if cnt == 1:
                    nums[i+1] = nums[j]
                    i += 1
                    j += 1
                    cnt = 2
                elif cnt == 2:
                    j += 1
                    
        return i + 1
                    
        