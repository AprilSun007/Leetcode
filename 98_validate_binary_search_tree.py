#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:02:42 2020

@author: jinwensun
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        val_list = self.traverse(root)
        pre = None
        for v in val_list:
            if v is None:
                continue
            else:
                if pre is None:
                    pre = v
                else:
                    if pre >= v:
                        return False
                    else:
                        pre = v
                        
        return True
        
    def traverse(self, root):
        
        if root is None:
            return [None]
        
        left_list = self.traverse(root.left)
        right_list = self.traverse(root.right)
        
        return left_list + [root.val] + right_list
        
    
# improved version
        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.last_node = None 
        return self.traverse(root)
        
    def traverse(self, root):
        
        if root is None:
            return True
        
        valid_l = self.traverse(root.left)
        #here last node is the node that you visited on the left subtree
        if (self.last_node is not None) and (self.last_node.val >= root.val):
            return False
        self.last_node = root
        valid_r = self.traverse(root.right)
        
        return (valid_l and valid_r)