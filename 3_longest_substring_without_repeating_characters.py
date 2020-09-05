#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:39:50 2020

@author: jinwensun
"""

class Solution0(object):
    def lengthOfLongestSubstring(self, s):
        
        
        if s is None :
            return 0
        if len(s) <= 1:
            return len(s)
        
        i = 0
        j = i+1
        seen = dict()
        seen[s[i]] = i
        max_len = 1
        while(i < j) and (j < len(s)):
            if (s[j] not in seen):
                max_len = max(max_len, j-i+1)
                seen[s[j]] = j
                j += 1
            else:
                i = seen[s[j]]+1
                max_len = max(max_len, j-i+1)
                seen = dict()
                for z in range(i, j+1):
                    seen[s[z]] = z
                j += 1
                
        return max_len      


#improved version of Solution0
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        : time complexity: O(n)
        : Space Complexity: O(m) m is the number of distinct letters in s
        """
        
        if s is None or len(s) == 0:
            return 0
        
        seen = dict()
        max_len = 1
        i = 0
        j = i
        while(i<j) and (j < len(s)):
            if j == 0:
                seen[s[j]] = j
            else:
                if (s[j] in seen) and (seen[s[j]] >= i):
                    i = seen[s[j]] + 1                    
                else:
                    max_len = max(max_len, j-i+1)
                    
                seen[s[j]] = j
            j += 1
                                    
        return max_len      

        
if __name__ == '__main__':
    sol = Solution1()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
    
  