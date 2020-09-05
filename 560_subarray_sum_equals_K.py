#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:33:45 2020

@author: jinwensun
"""

class Solution0(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        : Time Complexity O(n^2) python version will ETL
        """
        
        sum_table = []
        cnt = 0
        for i in range(len(nums)):
            sum_table.append(sum(nums[0:i+1]))
            if sum_table[i] == k:
                cnt += 1
               
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (sum_table[j] - sum_table[i] == k):
                    cnt += 1
                    
        return cnt
    
# improved version 
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        : time complexity: O(n)
        """
        sum_table = dict()
        
        cnt = 0
        cum_sum = 0
        sum_table[0] = 1
        for i in range(len(nums)):
            cum_sum += nums[i]
            
            target_sum = cum_sum - k
            if target_sum in sum_table:
                cnt += sum_table[target_sum]
                
            if cum_sum in sum_table:
                sum_table[cum_sum] += 1
            else:
                sum_table[cum_sum] = 1
                    
        return cnt