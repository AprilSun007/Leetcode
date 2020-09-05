#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 01:12:44 2020

@author: jinwensun
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        strt_ptr = 0
        end_ptr = len(numbers) - 1
        
        while(strt_ptr <= end_ptr):
            
            if(numbers[strt_ptr] + numbers[end_ptr] == target):
                return [strt_ptr+1, end_ptr+1]
            
            if(numbers[strt_ptr] + numbers[end_ptr] > target):
                end_ptr = end_ptr - 1
                
            elif(numbers[strt_ptr] + numbers[end_ptr] < target):
                strt_ptr = strt_ptr + 1
                
        if numbers[strt_ptr] == target:
            return strt_ptr + 1
        else:
            return 0