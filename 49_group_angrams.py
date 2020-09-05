#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:18:51 2020

@author: jinwensun
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        :Time Complexity: N*K(logK) N is the length of strs, 
            K is the max length of the word in strs
        :Space Complexity: O(NK)
        """
        
        result = dict()
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]
                
        
                
        return [v for i, (k, v) in enumerate(result.items())]
        
    
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))