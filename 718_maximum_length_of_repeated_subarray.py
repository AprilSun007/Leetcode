#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:44:47 2020

@author: jinwensun
"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        
        #dp[i][j] represents the length of longest sub-array between A[:i+1], B[:j+1],
        # on the condition that A[i] = B[j]
        # so dp[i][j] = dp[i-1][j-1] + 1
            
            
        for i in range(1, len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
        return max([max(r) for r in dp])
                