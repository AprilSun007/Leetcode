#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 00:42:00 2020

@author: jinwensun
"""

class Solution0(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if (nums is None) or (len(nums) == 0):
            return 0
        if nums[0] >= s:
            return 1
        
        ptr1 = 0
        ptr2 = 1
        min_len = 0
        
        while ptr2 < len(nums):
            
            if sum(nums[ptr1 : (ptr2+1)]) < s:
                ptr2 = ptr2 + 1
                
            if sum(nums[ptr1 : (ptr2+1)]) >= s:
                if min_len == 0:
                    min_len = ptr2-ptr1+1
                else:
                    min_len = min(min_len, ptr2-ptr1+1)
                if ptr1 == ptr2:
                    return 1
                ptr1 = ptr1 + 1
                
        return min_len
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
# 改进版 上一个每次循环都算sum， 那每次loop nums[ptr1 : (ptr2+1)] 都是O(k)， 太慢， 存一个total 更快， 但是algo 也复杂了些
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if (nums is None) or (len(nums) == 0) or (sum(nums) < s):
            return 0
        
        i = 0
        j = 0
        min_len = sys.maxsize
        total = nums[0]
        
        while(i <= j):
            if total < s:
                if j == len(nums) - 1:
                    break
                j += 1
                total += nums[j]
            else:
                if i == j:
                    return 1
                min_len = min(min_len, (j - i + 1))
                total -= nums[i]
                i += 1
                                
        return min_len
        
           
if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,2,4,3]
    s = 7
    print(sol.minSubArrayLen(s, nums))
    
        