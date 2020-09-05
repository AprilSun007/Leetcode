#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:37:30 2020

@author: jinwensun
"""

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if (lists is None) or (len(lists) == 0):
            return None
        
        pq = []
        for head_node in lists:
            if head_node is not None:
                heapq.heappush(pq, (head_node.val, head_node))
            
        head = None
        cur_node = None
        while len(pq) > 0:
            val, node_ = heapq.heappop(pq)
            if head is None:
                head = node_
                cur_node = node_
            else:
                cur_node.next = node_
                cur_node = cur_node.next
            if node_.next is not None:
                heapq.heappush(pq, (node_.next.val, node_.next))
                
        return head
            