#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:03:10 2020

@author: jinwensun
"""

class Solution0(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return None
        
        if (a==0) and (b==0):
            return [c for i in range(len(nums))]
        
        if (a ==0) and (b > 0):
            return [a*n*n + b*n + c for n in nums]
        if (a ==0) and (b < 0):
            tmp = [a*n*n + b*n + c for n in nums]
            return tmp[::-1]
       
                
        local_optimum = (-0.5)*b/a        
        result = []
        if (nums[0] > local_optimum and a > 0) or (nums[-1] < local_optimum and a < 0):
            return [a*n*n + b*n + c for n in nums]
        elif (nums[0] > local_optimum and a < 0) or (nums[-1] < local_optimum and a > 0):
            tmp = [a*n*n + b*n + c for n in nums]
            return tmp[::-1]
       
        else:
            dist = [abs(n - local_optimum) for n in nums]
            mid = 0
            while(dist[mid+1] <= dist[mid]):
                mid += 1
                if mid == len(nums)-1:
                    break
        
            result.append(a*nums[mid]*nums[mid] + b*nums[mid] + c)
            i = mid - 1
            j = mid + 1
            while(i >= 0):
                if j == len(nums):
                    result.append(a*nums[i]*nums[i] + b*nums[i] + c)
                    i -= 1
                else:                        
                    if dist[i] <= dist[j]:
                        result.append(a*nums[i]*nums[i] + b*nums[i] + c)
                        i -= 1
                    else:
                        result.append(a*nums[j]*nums[j] + b*nums[j] + c)
                        j += 1
                        
            
            while (j < len(nums)):
                result.append(a*nums[j]*nums[j] + b*nums[j] + c)
                j += 1
                
            if a > 0:
                return result
            else:
                return result[::-1]
# 不需要从中间走 两遍走就可以            
class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        res = [None] * len(nums)
        if a == 0 and b >=0:
            return [b * x + c for x in nums]
        if a == 0 and b < 0:
            return ([b * x + c for x in nums])[::-1]
        pivot = (b / 2 / a) * (-1)
        left, right, tail = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            if abs(nums[left] - pivot) > abs(nums[right] - pivot):
                res[tail] = a * nums[left] ** 2 + b * nums[left] + c 
                left += 1
            else:
                res[tail] = a * nums[right] ** 2 + b * nums[right] + c 
                right -= 1
            tail -= 1
        if a > 0: return res
        return res[::-1]
            
if __name__ == '__main__':
    nums = [-4,-2,2,4]
    a = 1
    b = 3
    c = 5
    
    s = Solution()
    print(s.sortTransformedArray(nums, a, b, c))
                
                        
                    
                        
            