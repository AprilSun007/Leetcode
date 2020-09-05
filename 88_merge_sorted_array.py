#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:47:07 2020

@author: jinwensun
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:        
            i = 0
            j = 0
            nums1_end = m
            while (i < nums1_end) and (j < n):
                if nums1[i] <= nums2[j]:
                    i += 1               
                else:
                    tmp = nums1[i:]
                    nums1[i] = nums2[j]
                    j+=1
                    nums1[(i+1):] = tmp[: -1]
                    i+=1
                    nums1_end +=1

            if (i == nums1_end ) and (j < n):
                nums1[i:] = nums2[j:]
                            
                
if __name__ == '__main__':
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    s = Solution()
    print(s.merge(nums1, m, nums2, n))