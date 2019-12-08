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
import math
class Solution_final(object):
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
    
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        num_strt = nums[0]
        num_end = nums[-1]
        
        mid = int(math.floor(len(nums)/2))
        num_mid = nums[mid]
        
        if target == num_strt:
            return 0
        elif target == num_end:
            return len(nums) - 1
        elif target == num_mid:
            return mid
        elif len(nums) == 2 or len(nums) == 1:
            return -1
        elif num_strt < num_mid:
            if num_strt < target and num_mid > target:
                ind = self.binary_search(nums[0: mid], target) 
                return ind
            else:
                ind = self.search(nums[(mid+1): ],target)
                if ind == -1:
                    return -1
                else: 
                    return ind + mid + 1
        elif num_strt > num_mid:
            if num_strt > num_mid:
                if num_mid < target and target < num_end:
                    ind = self.binary_search(nums[(mid+1) : ], target)
                    if ind == -1:
                        return -1
                    else: 
                        return ind + mid + 1
                else:
                    ind = self.search(nums[0:mid], target)
                    return ind
                    
    def binary_search(self, nums, target):
        
        mid = int(math.floor(len(nums) / 2) )
        
        if target == nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif len(nums) == 2 or len(nums) == 1:
            return -1
        
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            ind = self.binary_search(nums[0:mid], target)
            return ind
        elif target > nums[mid]:
            ind = self.binary_search(nums[(mid + 1): ],target)
            if ind == -1:
                return ind
            else:
                return ind + mid + 1

# ------------------  LeetCode Solutions ----------------------------#         
class Solution_onePass:
    def search(self, nums, target) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]: 
                    start = mid + 1
                else:
                    end = mid - 1
        return -1



class Solution_binarySearch:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
                
        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 
        
        rotate_index = find_rotate_index(0, n - 1)
        
        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)

            
        
if __name__ == '__main__':
    nums = [1,3,5]
    target = 0
    s = Solution_final()
    #print(s.twoSum_ptr(nums, 0, False))
    print(s.search(nums, target))       
        
                    
                
            
            
        
        
        