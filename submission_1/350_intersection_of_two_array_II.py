#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:35:51 2019

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

@author: jinwensun
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        result = []
        nums_dict1 = {}
        for n in nums1:
            if n in nums_dict1.keys():
                nums_dict1[n] = nums_dict1[n] + 1
            else:
                nums_dict1[n] = 1
                
        for n in nums2:
            if n in nums_dict1.keys() and nums_dict1[n] > 0:
                result.append(n)
                nums_dict1[n] = nums_dict1[n] -1
                
        return result
    
if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    s = Solution()
    #print(s.twoSum_ptr(nums, 0, False))
    print(s.intersect(nums1, nums2))          
        
                