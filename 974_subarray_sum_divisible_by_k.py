#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:07:23 2020

@author: jinwensun
"""

class Solution0(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        :time complexity: O(n)
        """
        
        cum_sum_table = dict()
        cum_sum = 0
        result = 0
        for i in range(len(A)):
            cum_sum += A[i]
            if cum_sum%K in cum_sum_table:
                cum_sum_table[cum_sum%K].append(i)
                result = result + len(cum_sum_table[cum_sum%K]) - 1
            else:
                cum_sum_table[cum_sum%K] = [i]
       
        if 0 in cum_sum_table:
            result += len(cum_sum_table[0])
            
        return result
                
                
                
# A cleaner solution using Counter
from collections import Counter          
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        : time complexity; O(n)
        """
                
        resid_list = []
        cum_sum = 0
        for i in range(len(A)):
            cum_sum += A[i]
            resid_list.append(cum_sum%K)
            
        resid_dict = Counter(resid_list)
        result = 0
        for key, value in resid_dict.items():
            if key != 0:
                result += value * (value - 1)/2
            if key == 0:
                result = result + value * (value - 1)/2 + value
                   
        return result   
                
                
            
        