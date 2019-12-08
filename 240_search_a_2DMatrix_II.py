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
import math
class Solution_final:
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
        
        
        
class Solution(object):
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
        
        n_rows = len(matrix)
        mid = int(math.floor((n_rows-1)/2))
        
        index_upper = False
        index_lower = False
        
        if matrix[mid][-1] > target:
            index_upper = self.searchMatrix(matrix[0:(mid + 1)], target)
        elif matrix[mid][-1] == target:
            return True
            
            
            
        if matrix[mid+1][0] < target:
            index_lower = self.searchMatrix(matrix[(mid+1):], target)
        elif matrix[mid+1][0] == target:
            return True
        
                        
        return (index_upper or index_lower)
    
# ------------------------ Leedcode ---------------------------- #
class Solution_BinarySearch:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi)//2
            if vertical: # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False
        
class Solution_DivideConquer:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right-left)//2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            
            return search_rec(left, row, mid-1, down) or search_rec(mid+1, up, right, row-1)

        return search_rec(0, 0, len(matrix[0])-1, len(matrix)-1)  

class Solution_SpaceReduction:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height-1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False      
        
if __name__ == '__main__':
    nums = [[5],[6]]

    target = 6
    s = Solution_final()
    #print(s.twoSum_ptr(nums, 0, False))
    print(s.searchMatrix(nums, target))          
        
        
        