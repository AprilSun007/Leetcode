#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:18:47 2020

@author: jinwensun
"""

# devide & conquer method
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.dfs(root)
        
    def dfs(self, root):
        
        if root is None:
            return []
        if (root.left is None) and (root.right is None):
            return [str(root.val)]
        
        left_path = self.dfs(root.left)
        right_path = self.dfs(root.right)
        
        path = []
        for p in left_path:
            path.append(str(root.val) + '->' + p)
        for p in right_path:
            path.append(str(root.val) + '->' + p)
            
        return path

# a recursive way    
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        path = None
        
        self.dfs(root, path)
        return self.result
        
        
    def dfs(self, root, path):
        
        if root is None:
            return 
        
        if path is None:
            path = str(root.val)
        else:
            path = path + '->' + str(root.val)
            
        if (root.left is None) and (root.right is None):
            if len(self.result) == 0:
                self.result = [path]
            else:
                self.result.append(path)
        if root.left is not None:
            self.dfs(root.left, path)
        if root.right is not None:
            self.dfs(root.right, path)
        
        
        