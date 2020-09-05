#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:01:45 2020

@author: jinwensun
"""

from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        result = defaultdict(list)
        
        for file_path in paths:
            fp = file_path.split(' ')
            if len(fp) == 1:
                direct = ''
                f = fp[0]
                result[f[f.find("(")+1:f.find(")")]].append(f[0:f.find("(")]) 
            else:
                direct = fp[0]
                for f in fp[1:]:
                    result[f[f.find("(")+1:f.find(")")]].append(direct + '/' + f[0:f.find("(")])
                    
        return [result[k] for k,v in result.items() if len(v) > 1]
     