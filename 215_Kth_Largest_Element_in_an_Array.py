#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:34:50 2020

@author: jinwensun
"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)

"""
class Solution(object):
    def findKthLargest(self, nums, k):
        
        return self.select(nums, len(nums) - k)
   
    def select(self, nums, k):
        
        nums, i = self.partition(nums)
        if i == k:
            return nums[i]
        elif i < k:
            return self.select(nums[i:], k-i)
        else:
            return self.select(nums[:i], k)      
        
    def partition(self, nums):
        
        if (nums is None) and (len(nums) == 0):
            return None
        
        pivot_val = nums[0]
        left_ptr = 0
        right_ptr = len(nums)-1
        
        
        while left_ptr < right_ptr:
            
            if (nums[left_ptr] > pivot_val) and (nums[right_ptr] < pivot_val):
                tmp = nums[left_ptr]
                nums[left_ptr] = nums[right_ptr]
                nums[right_ptr] = tmp
                left_ptr = left_ptr + 1
                right_ptr = right_ptr - 1
            else:                
                if (nums[left_ptr] <= pivot_val):
                    left_ptr = left_ptr + 1
                if (nums[right_ptr] >= pivot_val):
                    right_ptr = right_ptr - 1
                
        nums[0] = nums[right_ptr]
        nums[right_ptr] = pivot_val
        
        return nums, right_ptr
"""    
if __name__ == '__main__':
    
    nums = [3,2,1,5,6,4]
    k = 2
    
    s = Solution()
    print(s.findKthLargest(nums, k))
                
