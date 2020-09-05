#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:45:24 2020

@author: jinwensun
"""

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        time complexity: O(n)
        space complexity: O(n) (from result)
        """
        
        if root is None:
            return []
        
        # BFS, so use a queue for FIFO
        que = deque([root])
        result = []
        
        while len(que) >0:            
            # process level by level
            # the number of nodes need to be processed is the number of nodes on the queue
            level_result = []
            for i in range(len(que)):
                # pop at the current level
                node_ = que.popleft()
                level_result.append(node_.val)
                # add the nodes of the next level
                if node_.left is not None:
                    que.append(node_.left)                    
                if node_.right is not None :
                    que.append(node_.right)
            # add the current level result to result        
            result.append(level_result)   
            
        return result
            