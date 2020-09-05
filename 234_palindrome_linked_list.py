#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:49:08 2020

@author: jinwensun
"""

class Solution(object):
    def reverse(self, head):
        if (head is None) or (head.val is None):
            return None
        if (head.next is None):
            return head
        
        ptr1 = head
        ptr2 = head.next
        head.next = None        
        while(ptr2 is not None):
            if ptr2.next is not None:
                tmp = ptr2.next
                ptr2.next = ptr1
                ptr1 = ptr2
                ptr2 = tmp
            else:
                ptr2.next = ptr1
                return ptr2
        
        
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None) or (head.val is None) :
            return True
        
        ptr1 = head
        ptr2 = head
        
        while(ptr2 is not None) and (ptr2.next is not None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            
            
        head2 = ptr1
        list_end = self.reverse(head2)
        
        strt_ptr = head
        end_ptr = list_end
        
        while((strt_ptr is not None) and (end_ptr is not None)):
            
            if (strt_ptr.val != end_ptr.val):
                return False
            else:
                strt_ptr = strt_ptr.next
                end_ptr = end_ptr.next
                
        return True