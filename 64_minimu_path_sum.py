#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:00:33 2020

@author: jinwensun
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        :Time Complexity: O(mn)
        :Space Complexity: O(mn)
        
        Analysis
        --------
        DP: f(i, j) = min (f(i, j-1), f(i-1, j)) + grid[i, j]
            Initial Condition: f(0,0) = grid[0,0]
                               f(0,1) = grid[0,0] + grid[0,1]
                               f(1,0) = grid[0,0] + grid[1,0]
                               ...
        """
        if grid is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        if m == 1:
            return sum(grid[0])
        elif n == 1:
            total = 0
            for i in range(m):
                total = total + grid[i][0]
            return total
        
        f_matrix = []
        top = []
        for j in range(n):
            if j == 0:
                top.append(grid[0][j])
            else:
                top.append(grid[0][j] + top[j-1])
        f_matrix.append(top)
        left = []
        for i in range(m):
            if i == 0:
                left.append(grid[0][0])
            else:
                left.append(grid[i][0] + left[i-1])
                
        for i in range(1, m):
            f_matrix.append([left[i]] + [None]*(n-1))
            
        for i in range(1,m):
            for j in range(1,n):
                f_matrix[i][j] = min(f_matrix[i-1][j], f_matrix[i][j-1]) + grid[i][j]
                
        return f_matrix[-1][-1]
        
        