#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:56:00 2020

@author: jinwensun
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        :Time Complexity: O(amount * len(coins))
        :Space Complexity: O(amount * len(coins))
        """
        if amount == 0:
            return 1
        elif len(coins) == 0:
            return 0
        
        n = len(coins)
        DP = [[0]*(amount+1) for _ in range(n+1)]
        
        for i in range(n+1):
            DP[i][0] = 1
            
        for i in range(1, n+1):
            for j in range(1, amount+1):
                v = coins[i-1]
                k = 0
                while (j-v*k >= 0):
                    DP[i][j] = DP[i][j] + DP[i-1][j - v*k]
                    k = k+1
                    
        return DP[-1][-1]
    
    
if __name__=="__main__": 
    amount = 5
    coins = [1,2,5]
    s = Solution()
    print(s.change(amount, coins))