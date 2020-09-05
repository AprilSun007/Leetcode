#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:44:53 2020

@author: jinwensun
"""

class Solution(object):
    
    def findClosestElement(self, arr, x):
        
        if (len(arr) == 0) or (arr is None):
            return None
        
        strt = 0
        end = len(arr) - 1
        
        while(strt + 1 < end):
            
            mid = strt + (end - strt)//2
            
            if arr[mid] == x:
                return mid
            elif (arr[mid] < x) & (arr[mid + 1] > x):
                if (x - arr[mid]) <= arr[mid+1] - x:
                    return mid
                else:
                    return mid + 1
                
            elif (arr[mid] < x) & (arr[mid + 1] <= x):
                strt = mid
            elif arr[mid] > x:
                end = mid
                
        if (x - arr[strt]) <= arr[end] - x:
            return strt
        else:
            return end
        
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if (len(arr) == 0) or (arr is None):
            return []
        
        if arr[0] >= x:
            return arr[0 : k]
        if arr[-1] <= x:
            return arr[-1*k :]
        
        target_pos = self.findClosestElement(arr, x)
        
        strt = target_pos - 1
        end = target_pos + 1
        
        n = 1
        while(n < k):
            
            if end > len(arr) - 1:                
                d = k - n
                result = arr[(strt+1) : end]
                return (arr[(strt-d+1) : (strt+1)] + result)
            if strt < 0:
                d = k - n
                result = arr[(strt+1) : end]
                return (result + arr[end : (end + d)])
            
            if abs(arr[strt] - x) >  abs(arr[end] - x):
                end = end + 1
            elif abs(arr[strt] - x) <=  abs(arr[end] - x):
                strt = strt - 1
            n = n+1    
                         
        return arr[(strt+1) : end]
            
                            
        
    
if __name__ == '__main__':
    nums = [0,1,2,2,2,3,6,8,8,9]
    s = Solution()
    print(s.findClosestElement(nums,9))
    print(s.findClosestElements(nums,5,9))
  
    
"""
[0,1,2,2,2,3,6,8,8,9]
5
9
"""