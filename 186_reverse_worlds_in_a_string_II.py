#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:14:17 2020

@author: jinwensun
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if ((s is None) or (len(s) == 0)):
            return []
        
        s = self.reverse(s)
        strt_ptr = 0
        #end_ptr = strt_ptr
        
        for i in range(1, len(s)+1):
            if (i == len(s)) or (s[i] == ' '):
                s[strt_ptr : i] = self.reverse(s[strt_ptr : i])
                strt_ptr = i + 1
                
        """
        while (strt_ptr < len(s)):
            if end_ptr + 1 > len(s) - 1:
                break
            while (s[end_ptr + 1] != ' '):
                end_ptr = end_ptr + 1 
                if (end_ptr >= (len(s) - 1)):
                    break
            s[strt_ptr : (end_ptr + 1)] = self.reverse(s[strt_ptr : (end_ptr + 1)])
            strt_ptr = end_ptr + 2
            end_ptr = strt_ptr
        """
        
        return s
                    
    def reverse(self,s):
        if ((s is None) or (len(s) == 0)):
            return []
        
        strt_ptr = 0
        end_ptr = len(s) - 1
        
        while(strt_ptr < end_ptr):
            tmp = s[strt_ptr]
            s[strt_ptr] = s[end_ptr]
            s[end_ptr] = tmp
            
            strt_ptr = strt_ptr + 1
            end_ptr = end_ptr - 1
            
        return s
        
if __name__ == '__main__':
    
    s = Solution()
    sent = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    #print(s.reverse(sent))
    print(s.reverseWords(sent))
    
    