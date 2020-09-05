#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 00:29:41 2020

@author: jinwensun
"""

import heapq
class Solution0(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_dict = dict()
        for wd in words:
            if wd in word_dict:
                word_dict[wd] += 1
            else:
                word_dict[wd] = 1
                
        pq = []
        for i, (key, v) in enumerate(word_dict.items()):
            heapq.heappush(pq, (-1* v,key))
            
        result = []
        while len(result) < k:
            result.append(heapq.heappop(pq)[1])
            
        return result
    
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt_dict = Counter(words)
        r = cnt_dict.most_common(k)
        
        result =[]
        for r_ in r:
            result.append(r_[0])
        return result
            
     
        
     
if __name__ == '__main__':
    s = Solution0()
    #words = ["i", "love", "leetcode", "i", "love", "coding"]
    words = ["aaa",  "a","aa"]
    k = 1
    print(s.topKFrequent(words, k))
        