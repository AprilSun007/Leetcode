#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:40:16 2020

@author: jinwensun
"""

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        dp = dict()
        
        for word in sorted(words, key = len): # sort time complexity: nlog(n), loop time: n*s*s (the second s is word[0:i]+word[i+1:])
            
            l = len(word)
            max_len = 1
            for i in range(l):
                word_tmp = word[0:i] + word[i+1:]
                max_len = max(max_len, dp.get(word_tmp, 0) + 1)
            dp[word] = max_len
            
        return max(dp.values()) # time: O(n)
                
            
        