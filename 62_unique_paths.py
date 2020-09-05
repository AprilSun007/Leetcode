#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:06:23 2020

@author: jinwensun
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        :Time Complexity: O(mn)
        :Space Complexity: O(mn) 
        """
        if (m == 1) or (n == 1):
            return 1
        
        DP = [[0]*n for _ in range(m)]
        
        for i in range(m):
            DP[i][0] = 1
            
        for j in range(n):
            DP[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
                
        return DP[-1][-1]