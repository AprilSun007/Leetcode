#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:05:27 2020

@author: jinwensun
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return None
        
        i = head
        j = head
        
        while((j is not None) and (j.next is not None)):
          
            i = i.next
            j = j.next.next
            if i == j:
                break
            
        if (j is None) or (j.next is None):
            return None
            
        z = head
        while(z != i):
            z = z.next
            i = i.next
        return i
        
        
        
        