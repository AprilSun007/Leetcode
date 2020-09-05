#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:33:33 2020

@author: jinwensun
"""
# Time exceeds limit
class Solution0(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity O(n^2)
        """
        
        cum_sum = [0]
        
        for i in range(len(nums)):
            if i == 0:
                cum_sum.append(nums[0])
            else:
                cum_sum.append(cum_sum[i] + nums[i])
        
        max_len = 0
        for i in range(len(nums), 1, -1):
            if i%2 == 0:
                strt = 0
            else:
                strt = 1
                
            while(strt < i):
                if cum_sum[i] - cum_sum[strt] == (i-strt)/2:
                    max_len = max(max_len, i-strt)
                    break
                strt += 2
        
        return max_len
    
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity O(n)
        """
        
        counter_dict = dict()
        max_len = 0
        ct = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ct -= 1
            elif nums[i] == 1:
                ct += 1
            if ct == 0:
                max_len = max(max_len, i+1)
            elif ct in counter_dict:
                max_len = max(max_len, i - counter_dict[ct])
            else:
                counter_dict[ct] = i
                
        return max_len
            
            
                
        
            
                
        