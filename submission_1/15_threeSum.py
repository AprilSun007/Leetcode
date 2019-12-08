# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import itertools
class Solution(object):
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        if len(nums) == 0:
            return []
        elif nums[0] > 0:
            return []
        elif nums[-1] < 0:
            return []
        else:
            result = []
            for i in range(len(nums)):
                n = nums[i]
                if i >= 1 and n == nums[i - 1] :
                    continue
                
                target = 0 - n
                strt_ptr = i + 1
                end_ptr = len(nums) - 1
        
                while strt_ptr < end_ptr:                    
                    x1 = nums[strt_ptr]
                    x2 = nums[end_ptr]
            
                    if x1 + x2 == target:
                        if len(result) == 0:
                            result = [[n,x1,x2]]
                        else:
                            result.append([n, x1, x2])
                        strt_ptr = strt_ptr + 1
                        end_ptr = end_ptr - 1
                    elif x1 + x2 < target:
                        strt_ptr = strt_ptr + 1
                    elif x1 + x2 > target:
                        end_ptr = end_ptr - 1
        
        result = list(k for k,_ in itertools.groupby(result))       
        return result
    
    

if __name__ == '__main__':
    nums = [3,0,-2,-1,1,2]
    s = Solution()
    #print(s.twoSum_ptr(nums, 0, False))
    print(s.threeSum(nums))
