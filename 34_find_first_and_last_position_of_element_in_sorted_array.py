#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:41:46 2020

@author: jinwensun
"""

class Solution(object):
    
    def searchLeft(self, nums, target):
        
        if nums is None or len(nums) == 0:
            return -1
        
        strt = 0
        end = len(nums) - 1
        
        while(strt + 1 < end):
            mid = strt + (end - strt)//2
            
            if nums[mid] < target:
                strt = mid
            elif nums[mid] > target:
                end = mid
            elif (nums[mid] == target) & (nums[mid - 1] < target):
                return mid
            elif (nums[mid] == target) & (nums[mid - 1] == target):
                end = mid
        
        if nums[strt] == target:
            return strt
        if nums[end] == target:
            return end
        
        return -1
    
    def searchRight(self, nums, target):
        
        if nums is None or len(nums) == 0:
            return -1
        
        strt = 0
        end = len(nums) - 1
        
        while(strt + 1 < end):
            
            mid = strt + (end - strt)//2
            if nums[mid] < target:
                strt = mid
            elif nums[mid] > target:
                end = mid
            elif (nums[mid] == target) & (nums[mid + 1] > target):
                return mid
            elif (nums[mid] == target )& (nums[mid + 1] == target):
                strt = mid
        
        if nums[end] == target:
            return end
        if nums[strt] == target:
            return strt
               
        return -1
           
        
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if nums is None or len(nums) == 0 :
            return [-1, -1]
        
        
        strt = 0
        end = len(nums) - 1
        
        while(strt + 1 < end):
            #print((strt, end))
            mid = strt + (end - strt)//2
            #print(mid)
            if nums[mid] < target:
                strt = mid 
            elif nums[mid] > target:
                end = mid 
            elif nums[mid] == target:
                if (nums[mid -1] < target) & (nums[mid + 1] > target):
                    return[mid, mid]
                elif (nums[mid -1] == target) & (nums[mid + 1] == target):
                    return [(self.searchLeft(nums[strt: mid], target) + strt), (self.searchRight(nums[(mid+1) : (end+1)], target) + mid + 1)]
                elif nums[mid - 1] < target:
                    return [mid, (self.searchRight(nums[mid : (end+1)], target) + mid)] 
                elif nums[mid + 1] > target:
                    return [(self.searchLeft(nums[strt: (mid+1)], target) + strt), mid]
            
                    
        if (nums[strt] == target) & (nums[end] == target):
            return[strt, end]
        elif nums[strt] == target:
            return[strt, strt]
        elif nums[end] == target:
            return[end, end]
        else:
            return [-1, -1]
                
                    
if __name__ == '__main__':
    nums = [3,3,3]
    s = Solution()
    print(s.searchLeft(nums,3))
    print(s.searchRight(nums,3))
    print(s.searchRange(nums, 3))
    
      