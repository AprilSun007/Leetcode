#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:53:37 2020

@author: jinwensun
"""

from collections import Counter 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s is None or len(s) < len(p):
            return []
        
        result = []
        c_p = Counter(p)
        c_s = Counter()
        for i in range(len(s)):
            c_s[s[i]] += 1
            
            if i < len(p) -1:
                continue
            elif i == len(p) -1:
                if c_s == c_p:
                    result.append(0)
            else:
                c_s[s[i-len(p)]] -= 1
                if c_s[s[i-len(p)]]  == 0:
                    del c_s[s[i-len(p)]]
                if c_s == c_p:
                    result.append(i -len(p) + 1)
                    
        return result
                
                
            
                
        