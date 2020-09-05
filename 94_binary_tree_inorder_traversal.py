#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:59:31 2020

@author: jinwensun
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        
        if left is None:
            left = []
        if right is None:
            right = []
            
        return left + [root.val] + right
        