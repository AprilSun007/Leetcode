#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:59:02 2020

@author: jinwensun
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        left_min_depth = self.minDepth(root.left)
        right_min_depth = self.minDepth(root.right)
        
        if (left_min_depth == 0) and (right_min_depth == 0):
            return 1
        elif left_min_depth == 0:
            return right_min_depth + 1
        elif right_min_depth == 0:
            return left_min_depth + 1
        else:        
            return min(left_min_depth, right_min_depth)+1
        