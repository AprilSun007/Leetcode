#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:15:35 2020

@author: jinwensun
"""

from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        :time complexity: O(N)
        : N is the number of domains in the cpdomains 
        """
        result = defaultdict(int)
        for v in cpdomains:
            n, d = v.split(' ')            
            d_list = d.split('.')
            for i in range(1, len(d_list)+1):
                d_ = '.'.join(d_list[(-1)*i:])
                result[d_] += int(n)
                
        return [str(v) + ' ' + k for k,v in result.items()]