#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:52:37 2020

@author: jinwensun
"""

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        # Check to see if there will be a solution
        n = len(stones)
        if (n-1) %(K-1) != 0:
            return -1
        
        # Get cumsum
        cum_sum = [0] * (n+1)
        for i in range(1, n+1):
            cum_sum[i] = cum_sum[i-1] + stones[i-1]
            
        #Construct 3D DP matrix
        DP = [[[float("inf")]* (K+1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            DP[i][i][1] = 0
            
        for length in range(2, n+1):
            
            for l in range(0, n-length +1):
                r = l + length - 1
                for k in range(2, K+1):
                    for m in range(l, r):
                        DP[l][r][k] = min(DP[l][r][k], DP[l][m][1] + DP[m+1][r][k-1])
                        
                if DP[l][r][K] < float("inf"):
                    DP[l][r][1] =DP[l][r][K] + cum_sum[r+1] - cum_sum[l]
                    
        return DP[0][-1][1]
    
    
if __name__ == '__main__':
    stones = [3,2,4,1]
    K = 2
    s = Solution()
    print(s.mergeStones(stones, K))