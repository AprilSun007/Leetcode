#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:56:10 2020

@author: jinwensun
"""
import collections
class Solution0(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        :time complextity: O(n)
        :Space complesity :O(1)
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
    
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        : time complextity: O(n)
        : Space Complesity: O(2)
        """
        if s is None or len(s) == 0:
            return -1
        seen = set()
        s_dict = dict()
        for i in range(len(s)):
            char = s[i]
            if char in seen:
                if char in s_dict:                
                    del s_dict[char]
            else:
                s_dict[char] = i
                
            seen.add(char) 
        
        if len(s_dict) == 0:
            return -1
        
        idx = []
        for k,v in s_dict.items():
            idx.append(v)
        
        return min(idx)
            
if __name__ == '__main__':
    s = "leetcode"
    sol = Solution()
    print(sol.firstUniqChar(s))