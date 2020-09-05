#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 00:37:08 2020

@author: jinwensun
"""
# iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        ptr1 = head
        ptr2 = head.next
        head.next = None
        
        while (ptr2 is not None):
            tmp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = tmp
            
        return ptr1
    
# recursively
            