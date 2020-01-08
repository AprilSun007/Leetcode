#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:51:52 2020

@author: jinwensun

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        if not nums:
            return []
        if len(nums) == 0:
            return []
        
        nums = [ -1 * n for n in nums]
        
        strt = 0
        end_ = k
        result = []
        
        while end_ <= len(nums):
            num = nums[strt : end_]
            if strt == 0:
                heaplist = [(j,i) for i, j in enumerate(num)]
                heapq.heapify(heaplist)
                result.append( (-1) * min(heaplist)[0])                
            else:
                new_value = nums[(end_ - 1)]
                idx = min(heaplist)[1]
                if idx in range(strt, end_):
                    if min(heaplist)[0] <= new_value:
                        result.append((-1) * min(heaplist)[0])
                    else:
                        heapq.heapreplace(heaplist, (new_value, (end_ - 1)))
                        result.append( (-1) * new_value)
                else:
                    heapq.heapreplace(heaplist, (new_value, (end_ - 1)))
                    result.append((-1) * min(heaplist)[0])
                    
            strt = strt + 1
            end_ = end_ + 1
            
        return result
    
if __name__ == '__main__':
    nums = [1,3,1,2,0,5]
    s = Solution()
    k = 3
    print(s.maxSlidingWindow(nums,k))            
            
            
            

                    