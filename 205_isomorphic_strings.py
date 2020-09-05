#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:18:51 2020

@author: jinwensun
"""

class Solution0(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_dict = dict()
        seen = set()
        for i in range(len(s)):
            if s[i] in map_dict:
                if map_dict[s[i]] != t[i]:
                    return False 
            else:                
                if t[i] in seen:
                    return False
                map_dict[s[i]] = t[i]
                seen.add(t[i])
                
        return True
    
# use zip to get the map pair, 
class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        