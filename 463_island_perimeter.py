#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:05:56 2020

@author: jinwensun
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        : time complexity: O(mn)
        """
        if grid is None or len(grid) == 0:
            return 0
        
        perim = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0:
                        up = 0
                    else:
                        up = grid[i-1][j]
                    if i == len(grid) - 1:
                        down = 0
                    else:
                        down = grid[i+1][j]
                    if j == 0:
                        left = 0
                    else:
                        left = grid[i][j-1]
                    if j == len(grid[0]) - 1:
                        right = 0
                    else:
                        right = grid[i][j+1]
                    
                    perim += 4 - (up + down + left + right)
                        
                        
                        
                        
        return perim
                
        