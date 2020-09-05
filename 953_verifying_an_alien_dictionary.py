#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:59:34 2020

@author: jinwensun
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        word_dict = dict()
        
        # O(m)
        for i, letter in enumerate(order):
            word_dict[letter] = i
        word_dict["null"] = -1
            
        max_len = 0
        for i in range(len(words)):
            max_len = max(max_len, words[i])
        
        i = 0
        continue_ind = True
        
        while continue_ind and (i< max_len):
            equal_ind = 0
            for j in range(len(words) -1):
                if i < len(words[j]): 
                    letter1 = words[j][i]
                else:
                    letter1 = "null"
                
                if i < len(words[j+1]): 
                    letter2 = words[j+1][i]
                else:
                    letter2 = "null"
                    
                if word_dict[letter1] > word_dict[letter2]:
                    return False
                if word_dict[letter1] == word_dict[letter2]:
                    equal_ind = 1
                    
            if equal_ind == 1:
                continue_ind = True
                i += 1
            else:
                continue_ind = False
                
        return True
                
                
                
                
            
            
            
        