#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 23:36:34 2020

@author: jinwensun
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        :Time Complexity: O(len(word1)*len(word2))
        :Space Complexity: O(len(word1)*len(word2))
        """
        
        if word1 == word2:
            return 0
        if (len(word1) == 0) or (len(word2) == 0):
            return max(len(word1), len(word2))
        
        DP = [[0]*len(word2) for _ in range(len(word1))]
        
        if word1[0] == word2[0]:
            DP[0]= [x for x in range(len(word2))]
            for i in range(1,len(word1)):
                DP[i][0] = DP[i-1][0]+1
                
        else:
            DP[0][0] = 1   
            ind = True
            for i in range(1, len(word1)):
                if (word1[i] == word2[0]) and ind:
                    # There will be only one time we count it as equal
                    # Once  this happened, the second time equal doesn't count 
                    # anymore
                    DP[i][0] = DP[i-1][0]
                    ind = False
                else:
                    DP[i][0] = DP[i-1][0] + 1
            ind = True
            for j in range(1, len(word2)):
                if (word2[j] == word1[0]) and ind:
                    DP[0][j] = DP[0][j-1]
                    ind = False
                else:
                    DP[0][j] = DP[0][j-1] + 1
                    
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    DP[i][j] = min(DP[i-1][j-1], DP[i][j-1]+1, DP[i-1][j]+1)
                else:
                    DP[i][j] = min(DP[i-1][j-1], DP[i][j-1], DP[i-1][j]) +1
                    
        return DP[-1][-1]

# Improved version    
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        
        Thought
        -------
        Comparing to the version that I wrote, this version add a common letter 
        at the front of both letters. This operation for sure wont change the 
        returned outcome. However, it makes initialing much for convinient.
        """
        
        if word1 == word2:
            return 0
        if (len(word1) == 0) or (len(word2) == 0):
            return max(len(word1), len(word2))
        
        DP = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        DP[0] = [x for x in range(len(word2)+1)]
        for i in range(len(word1)+1):
            DP[i][0] = i
                    
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = min(DP[i-1][j-1], DP[i][j-1]+1, DP[i-1][j]+1)
                else:
                    DP[i][j] = min(DP[i-1][j-1], DP[i][j-1], DP[i-1][j]) +1
                    
        return DP[-1][-1]
                    
        