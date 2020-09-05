#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:08:56 2020

@author: jinwensun
"""

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        asic_dict = dict()
        
        for s in strings:
            c_list = []
            for i in range(len(s)):
                if i == 0:
                    c_list.append(0)
                else:
                    c_list.append((ord(s[i]) - ord(s[0]))%26)
                    
            if tuple(c_list) in asic_dict:
                asic_dict[tuple(c_list)].append(s)
            else:
                asic_dict[tuple(c_list)] = [s]
                
        return asic_dict.values()
                
        