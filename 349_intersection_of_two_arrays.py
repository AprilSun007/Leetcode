#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:44:50 2020

@author: jinwensun
"""

from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        """
        result = []
        for k in c1.keys():
            if k in c2:
                result.append(k)
        """
        
        #return list(set(c1.keys()) & set(c2.keys())) equivalent to the following
        return list(set(c1.keys()).intersection(set(c2.keys())))
        