#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:57:16 2020

@author: jinwensun
"""

from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strt = 0
        end = 10
        
        dna_dict = defaultdict(int)
        while end <= len(s):
            sub_s = s[strt:end]
            dna_dict[sub_s] += 1
            strt += 1
            end += 1
            
        result = []
        for k, v in dna_dict.items():
            if v > 1:
                result.append(k)
                
        return result
    
if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    sol = Solution()
    print(sol.findRepeatedDnaSequences(s))