#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 00:49:17 2020

@author: jinwensun
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        ptr1 = head
        ptr2 = head.next
        
        while (ptr2 is not None):
            if ptr1 == ptr2:
                return True
            if ptr2.next is None:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
                       
        return False
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 二刷 无区别
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if (head is None) or (head.next is None):
            return False
        
        node_slow = head
        node_fast = head.next
        
        while((node_slow is not None) and (node_fast is not None)):
            if node_slow == node_fast:
                return True
            else:
                node_slow = node_slow.next
                if node_fast.next is None:
                    return False
                else:
                    node_fast = node_fast.next.next
        return False
            
        