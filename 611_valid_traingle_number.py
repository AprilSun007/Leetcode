#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 23:14:44 2020

@author: jinwensun
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :time complexity : O(n^2)
        """
        if nums is None or len(nums) < 3:
            return 0
        
        nums.sort()
        cnt = 0
        
        for strt in range(len(nums)-2):
            i = strt+1
            j = strt +2
            while(i < len(nums) - 1):
                while(j < len(nums)) and (nums[strt] + nums[i] > nums[j]):
                    j += 1
                   
                
                # 这里为什么会 j-i-1 有可能为负呢：这是因为在上一轮 j = i+1就已经不满足 nums[strt] + nums[i] > nums[j]
                # 然后 i+=1， 就会有 i = j，这个时候进入走里面的while：
                # 如果 nums【strt】！= 0: j 就会+1 完全没问题
                # 问题处在如果 nums【strt】 = 0， 又不会进入while，这个时候 j - i - 1 就会为负
                cnt += max(0, j - i -1)
                i += 1
                
        return cnt
                    
                
                    
if __name__ == '__main__':
    nums = [0,1,0]
    s = Solution()
    print(s.triangleNumber(nums))
            
    