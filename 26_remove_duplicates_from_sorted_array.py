#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:08:56 2020

@author: jinwensun
"""

class Solution0(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums is None) or (len(nums) == 0):
            return -1
        
        ptr1 = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[ptr1]:
                continue
            else:
                ptr1 = ptr1 + 1
                nums[ptr1] = nums[i]
                    
        return ptr1 + 1
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:27:36 2020

@author: jinwensun
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        
        while(j <= len(nums) - 1):
            if nums[j] == nums[i]:
                j +=1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1
                
        return i+1
    
if __name__ == '__main__':
    nums = [1,1,2]
    s = Solution()
    print(s.removeDuplicates(nums))
            