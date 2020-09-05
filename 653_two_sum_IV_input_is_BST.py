#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:22:33 2020

@author: jinwensun
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.tree = root
        return self.helper(root, k)
   
    def helper(self, root, k):
        if root is None:
            return False
        
        target = k - root.val
        
        if (self.dfs(self.tree, target, root)):
            return True
        else:
            return (self.helper(root.left, k) or self.helper(root.right, k))
        
        
    def dfs(self, root, k, first_node):
        
        if root is None:
            return False
        if (root.val == k) and (root != first_node):
            return True
        
        if root.val > k:
            return self.dfs(root.left, k, first_node)
        elif root.val < k:
            return self.dfs(root.right, k, first_node)
        