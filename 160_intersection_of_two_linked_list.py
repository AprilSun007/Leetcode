#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:57:07 2020

@author: jinwensun
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None) or (headB is None):
            return None
        
        ptr1 = headA
        ptr2 = headB
        endA = None
        endB = None
        
        
        while True:
            if ptr1 == ptr2:
                return ptr1
            
            if ptr1.next is None:
                endA = ptr1  
                ptr1 = headB
            else:
                ptr1 = ptr1.next
                
            if ptr2.next is None:
                endB = ptr2
                ptr2 = headA
            else:                       
                ptr2 = ptr2.next            
                
            if (endA is not None) and (endB is not None) and (endA != endB) :
                return None
                