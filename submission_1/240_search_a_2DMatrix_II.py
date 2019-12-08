#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:07:37 2019

240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

@author: jinwensun
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix) == 0:
            return False
        
        if len(matrix) == 1:
            return target in matrix[0]
        
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        
        n_row = len(matrix)
        n_col = len(matrix[0])
        
        
        x1 = n_row -1
        x2 = 0
        
        while x1 >= 0 and x2 < n_col:
            if matrix[x1][x2] == target:
                return True
            elif matrix[x1][x2] > target:
                x1 = x1 -1
            else:
                x2 = x2 + 1
        
        return False

if __name__ == '__main__':
    nums = [[5],[6]]

    target = 6
    s = Solution()
    #print(s.twoSum_ptr(nums, 0, False))
    print(s.searchMatrix(nums, target))          
        
        
        
