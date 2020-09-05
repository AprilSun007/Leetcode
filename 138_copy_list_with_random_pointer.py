#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:17:16 2020

@author: jinwensun
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head is None:
            return head
               
        visited_node_dict = dict()
        
        node = head
        while node is not None:
            if node in visited_node_dict:
                node_dup = visited_node_dict[node]
            else:
                node_dup = Node(node.val, None, None)
                visited_node_dict[node] = node_dup
            
            
            node_next = node.next
            node_rand = node.random
            if node_next in visited_node_dict:
                node_dup.next = visited_node_dict[node_next]
            elif node_next is not None:
                node_next_dup = Node(node_next.val,None, None)
                visited_node_dict[node_next] = node_next_dup
                node_dup.next = visited_node_dict[node_next]
                
            if node_rand in visited_node_dict:
                node_dup.random = visited_node_dict[node_rand]
            elif node_rand is not None:
                node_rand_dup = Node(node_rand.val,None, None)
                visited_node_dict[node_rand] = node_rand_dup
                node_dup.random = visited_node_dict[node_rand]
                
            node = node.next
            
        return visited_node_dict[head]
                
        