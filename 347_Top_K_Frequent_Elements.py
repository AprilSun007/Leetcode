#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:20:41 2020

@author: jinwensun

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import heapq
import collections

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
    

class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = dict()
        for n in nums:
            if n in nums_dict:
                nums_dict[n] = nums_dict[n] + 1
            else:
                nums_dict[n] = 1
                
        nums_dict2 = dict()
        for key in nums_dict:
            value = nums_dict[key]
            if value in nums_dict2:
                nums_dict2[value].append(key)
            else:
                nums_dict2[value] = []
                nums_dict2[value].append(key)
                
        pq = []
        for key in nums_dict2:
            heapq.heappush(pq,key)
        
        result = []
        for key in heapq.nlargest(k, pq):
            for i in nums_dict2[key]:
                result.append(i)
                if len(result) == k:
                    return result
        
            
                
if __name__ == '__main__':
    nums = [4,1,-1,2,-1,2,3]
    s = Solution()
    k = 2
    print(s.topKFrequent(nums,k))            
            
            