#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:40:21 2020

@author: jinwensun
"""

class Solution(object):
    
    def twoSumClosest(self, nums, target):
        
        #if (nums is None) or (len(nums) < 2):
            #return None
        
        strt_ptr = 0
        end_ptr = len(nums) - 1
        min_diff = None
        total = None
        while(strt_ptr < end_ptr):
            if (min_diff is None) or (min_diff > abs(target - nums[strt_ptr] - nums[end_ptr])):
                min_diff = abs(target - nums[strt_ptr] - nums[end_ptr])
                total = nums[strt_ptr] + nums[end_ptr]
                                
            if nums[strt_ptr] + nums[end_ptr] > target:
                end_ptr = end_ptr - 1
            elif nums[strt_ptr] + nums[end_ptr] < target:
                strt_ptr = strt_ptr + 1
            else:
                return [0,total]
        return [min_diff, total]
        
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (nums is None) or (len(nums) < 3):
            return None
        nums.sort()
        min_diff = None
        total = None
        for i in range(0, len(nums)-2):
            num = nums[i]
            if (min_diff is None) or (min_diff > self.twoSumClosest(nums[i+1:], target - num)[0]):
                min_diff, total_ = self.twoSumClosest(nums[i+1:], target - num)
                total = total_ + num
                
        return total
    
    
if __name__ == "__main__":
    
    s = Solution()
    
    nums = [-1,2,1,-4]
    
    print(s.threeSumClosest(nums, 1))

            
        