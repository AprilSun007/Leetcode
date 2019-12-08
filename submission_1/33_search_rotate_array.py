#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:08:28 2019

33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4



@author: jinwensun
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1        
        if target == nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif len(nums) == 2 or len(nums) == 1:
            return -1
        
        strt = 0
        end_ = len(nums) - 1
        
        while strt < end_:
            mid = (strt + end_)//2
            num_mid = nums[mid]
            num_strt = nums[strt]
            num_end = nums[end_]
            
            if target == num_mid:
                return mid
            
            if num_strt < num_mid:
                if num_strt <= target and num_mid > target:
                    end_ = mid                
                else:
                    strt = mid + 1
            elif num_strt > num_mid:
                if num_mid < target and target <= num_end:
                    strt = mid + 1
                else:
                    end_ = mid
        return -1

if __name__ == '__main__':
    nums = [1,3,5]
    target = 0
    s = Solution()
    #print(s.twoSum_ptr(nums, 0, False))
    print(s.search(nums, target))       
        
                    
                
            
            
        
        
        
