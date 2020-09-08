#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:05:31 2020

@author: jinwensun
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        def check(s, cnt):

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
                    if cnt >= 1:
                        return False
                    else:
                        cnt += 1
                        return check(s[(i+1) : (j+1)], cnt) or check(s[i: j], cnt)

                else:
                    i += 1
                    j -= 1

            return True
        
        return check(s, 0)
            
        
        
if __name__ == '__main__':
    s = 'abc'
    sol = Solution()
    print(sol.validPalindrome(s))