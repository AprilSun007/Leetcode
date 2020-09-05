#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:47:23 2020

@author: jinwensun
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        
        if (root == p) or (root == q):
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l is not None and r is not None:
            return root
        elif l is None and r is None:
            return None
        elif l is None:
            return r
        elif r is None:
            return l