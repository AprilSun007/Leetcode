#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:08:11 2020

@author: jinwensun
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x <=3:
            return 1
        
        i = 1
        j = x//2
        
        while i + 1 < j:
            mid = i + (j-i)//2
            
            if mid*mid > x:
                j = mid - 1
            elif mid*mid < x:
                i = mid
            else:
                return mid
            
        if i < j:
            if j * j <=x:
                return j
            else:
                return i
        else:
            return i
            
        return i
            
    
if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(8))