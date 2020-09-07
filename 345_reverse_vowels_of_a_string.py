#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:57:51 2020

@author: jinwensun
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (len(s) == 0) or (s is None):
            return s
        
        i = 0
        j = len(s) - 1
        sl = [c for c in s]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while(i < j):
            
            if sl[i] not in vowels:
                i += 1
            if sl[j] not in vowels:
                j -= 1 
                
            if (sl[i] in vowels) and (sl[j] in vowels):
                sl[i], sl[j] = sl[j], sl[i]
                i += 1
                j -= 1
                
        return ''.join(sl)
            
            
if __name__ == '__main__':
    s = 'hello'
    sol = Solution()
    print(sol.reverseVowels(s))