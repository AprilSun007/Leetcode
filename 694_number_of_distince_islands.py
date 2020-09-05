#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:51:47 2020

@author: jinwensun
"""

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        ：time complexity : O(R * C)
        """
        
        def dfs(r, c, r0, c0):           
            if (r >= 0) and (r < len(grid)) and ( c>= 0) and (c < len(grid[0])):
                if (r, c) not in seen:
                    seen.add((r,c))
                    if grid[r][c] == 1:
                        shape.append((r-r0, c-c0))
                        dfs(r+1, c, r0, c0)
                        dfs(r-1, c, r0, c0)
                        dfs(r, c+1, r0, c0)
                        dfs(r, c-1, r0, c0)
                        
        if grid is None or len(grid) == 0:
            return 0
        
        seen = set()
        shape_set = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((i, j) not in seen) and (grid[i][j] == 1):
                    shape = []
                    dfs(i,j,i,j)
                    if len(shape) > 0:
                        shape_set.add(tuple(shape))
        return len(shape_set)
                    
                        
    
                        
                
                
                