#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:42:49 2020

@author: jinwensun
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        nums.sort(reverse = True)
        cnt = 0
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            while(j < len(nums) - 1):
                while((k > j) and (nums[i] + nums[j] + nums[k] < target)):
                    k -= 1
                if j <= k:   
                    cnt += len(nums) - k - 1
                else:
                    cnt += len(nums) - j - 1
                j += 1
                
        return cnt
            
        
if __name__ == '__main__':
    nums = [1,-1,2,0,3,-2]
    target = 2
    s = Solution()
    print(s.threeSumSmaller(nums, target))