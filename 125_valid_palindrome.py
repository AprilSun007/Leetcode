#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:11:06 2020

@author: jinwensun
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        
        i = 0
        j = len(s) - 1
        while(i < j):
            while((not s[i].isalnum() )and (i<j)):
                i += 1
            while((not s[j].isalnum()) and (i < j)):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
                
        return True
            
        
        


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.isPalindrome(s))
        
        