#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:29:13 2020

@author: jinwensun
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
            
        left_child = self.invertTree(root.left)
        right_child = self.invertTree(root.right)  
        
        root.left = right_child
        root.right = left_child
        
        return root
        