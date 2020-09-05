#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:47:50 2020

@author: jinwensun
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if (height is None) or (len(height) == 0):
            return 0
        
        strt_ptr = 0
        end_ptr = len(height) - 1
        max_area = min(height[strt_ptr], height[end_ptr]) * (end_ptr - strt_ptr)
        
        while (strt_ptr < end_ptr):
            
            max_area = max(max_area, min(height[strt_ptr], height[end_ptr]) * (end_ptr - strt_ptr))
            
            if height[strt_ptr] <= height[end_ptr]:
                strt_ptr = strt_ptr + 1
            elif height[strt_ptr] > height[end_ptr]:
                end_ptr = end_ptr - 1
                
            
        
        return max_area