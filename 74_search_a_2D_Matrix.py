#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:37:10 2020

@author: jinwensun
"""

class Solution(object):
    
    def searchArray(self, arr, target):
        
        if (len(arr) == 0) or (arr is None):
            return False
        
        strt = 0
        end = len(arr) - 1
        
        while(strt + 1 < end):
            mid = strt + (end - strt)//2
            
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                strt = mid
            elif arr[mid]> target:
                end = mid
                
        if (arr[strt] == target) or (arr[end] == target):
            return True
        else:
            return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if (len(matrix) == 0) or (matrix is None):
            return False
        
        strt = 0
        end = len(matrix) -1
        
        while(strt + 1 < end):
            mid = strt + (end-strt)//2
            
            if (matrix[mid][0] <= target) and (matrix[mid][-1] >= target):
                return self.searchArray(matrix[mid], target)
            elif matrix[mid][0] > target:
                end = mid
            elif (matrix[mid][0] <= target) and (matrix[mid][-1] < target): 
                strt = mid
                
        return ((self.searchArray(matrix[strt], target)) or (self.searchArray(matrix[end], target)))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        