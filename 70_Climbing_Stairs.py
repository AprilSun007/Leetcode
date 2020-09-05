#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:15:49 2020

@author: jinwensun
"""
## Bottom Up Approach (Iterative)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        :Time Complexity: O(n)
        :Space Complexity: O(n)
        Thoughts
        ________
        DP: f(n) = f(n-1) + f(n-2)
            if use bottom-up approach: f(1) = 1 f(2) = 2
        """
        
        if n < 3:
            return n
        
        f_list = [0,1,2]
        for i in range(3, n+1):
            f_list.append(f_list[i-1] + f_list[i-2])
            
        return f_list[-1]
    
## Top Down Approach (Recursive)
        
class Solution(object):
   
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        :Time Complexity: O(n)
        :Space Complexity: O(n)
        Thoughts
        ________
        DP: f(n) = f(n-1) + f(n-2)
            if use bottom-up approach: f(1) = 1 f(2) = 2
        """
        if n < 3:
            return n
        
        f_list = [0,1,2]
        for i in range(3, n+1):
            f_list.append(None)
    
        def helper(n):
            
            if f_list[n] is not None:
                return f_list[n]
            else:
                if f_list[n-1] is None:
                    f_list[n-1] = helper(n-1)
                if f_list[n-2] is None:
                    f_list[n-2] = helper(n-2)
                f_list[n] = f_list[n-1] + f_list[n-2]
            return f_list[n]
                
        return helper(n)
                