#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:32:16 2020

@author: jinwensun
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        if (len(text1) == 0) or (len(text2) == 0):
            return 0
        
        n = len(text1)
        m = len(text2)
        
        DP = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]+1)
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])
                    
        return DP[-1][-1]
        