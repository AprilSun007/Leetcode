#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:15:18 2020

@author: jinwensun
"""

class Solution(object):
    def trimBST(self, root, L, R):
                
        return self.trim(root, L, R)
        
    
    def trim(self, node, L, R):
        if not node:
            return None
        elif node.val > R:
            return self.trim(node.left, L, R)
        elif node.val < L:
            return self.trim(node.right, L, R)
        else:
            node.left = self.trim(node.left, L, R)
            node.right = self.trim(node.right, L, R)
            
        return node
        