#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 19:17:58 2020

@author: jinwensun
"""
#using two pointers
class Solution0(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
                
            for j in range(i+1, len(nums)):
                if (j > i+1) and (nums[j] == nums[j-1]):
                    continue
                n1 = nums[i]
                n2 = nums[j]
                result_2sum = self.twoSum(nums[j+1:], target - n1 - n2)
                for r in result_2sum:
                    result.append([n1, n2] + r)
        return result     
                
                
    def twoSum(self, nums, target):
        
        if len(nums) <= 1 or nums is None:
            return set()
        
        ptr1 = 0
        ptr2 = len(nums) -1        
        result = []
        while ptr1 < ptr2:
            if nums[ptr1] + nums[ptr2] > target:
                v = nums[ptr2]
                while (v == nums[ptr2]) and (ptr2 > ptr1):
                    ptr2 -= 1
                
            elif nums[ptr1] + nums[ptr2] < target:
                v = nums[ptr1]
                while (v == nums[ptr1]) and (ptr1 < ptr2):
                    ptr1 += 1
                
            else:
                result.append([nums[ptr1], nums[ptr2]])
                v = nums[ptr1]
                while (v == nums[ptr1]) and (ptr1 < ptr2):
                    ptr1 += 1
                
        return result    
    
# using hashmap    
class Solution1(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = set()
        dup_outer = set()
        dict_2sum = dict()
        
        for i in range(len(nums)):
            n1 = nums[i]
            if n1 in dup_outer:
                continue
            dup_outer.add(n1)
            
            dup_inner1 = set()
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                if n2 in dup_inner1:
                    continue
                dup_inner1.add(n2)
                
                dup_inner2 = set()
                for z in range(j+1, len(nums)):
                    n3 = nums[z]
                    if n3 in dup_inner2:
                        continue
                    n4 = target - n1 - n2 - n3
                    
                    if n4 in dict_2sum and dict_2sum[n4] == str(i)+str(j):
                        result.add(tuple(sorted([n1,n2,n3,n4])))
                    dict_2sum[n3] = str(i)+str(j)
                    
        return [list(r) for r in result]