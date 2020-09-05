#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:41:57 2020

@author: jinwensun
"""

class Solution(object):
    
           
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if (nums is None) or (len(nums) <= 1):
            return nums
        
        n = len(nums) 
        k = k % n
        cnt = 0
        ptr1 = 0
        while(cnt < n):
            ptr2 = ptr1
            pre = nums[ptr2]            
            while True:
                tmp = nums[(ptr2 + k) % n]
                nums[(ptr2 + k) % n] = pre
                pre = tmp
                cnt = cnt + 1
                
                if ((ptr2 + k) % n == ptr1):
                    ptr1 = ptr1 + 1
                    break
                ptr2 = (ptr2 + k) % n
                
        return nums
                
if __name__ == '__main__':
    
    nums = [1,2,3,4,5,6]
    k = 2
    
    s = Solution()
    print(s.rotate(nums, k))
                