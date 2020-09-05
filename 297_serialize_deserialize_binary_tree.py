#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:34:35 2020

@author: jinwensun
"""

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        time complexity: O(N)
        space complexity: O(N)
        """
        if root is None:
            return ""
        
        que = deque([root])
        result = []
        
        while len(que) > 0:
            node_ = que.popleft()
            if node_ is not None:
                result.append(str(node_.val))
            else:
                result.append('null')
            
            if node_ is not None:
                que.append(node_.left)
                que.append(node_.right)
            
            
        return '['+','.join(result)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        time complexity: O(N)
        space complexity: O(N)
        """
        if data == "":
            return None
        # sparse the string to a list of tree nodes
        b_tree = [TreeNode(int(val)) if val != 'null' else None for val in data[1:-1].split(',')]
        
        parent_ptr = 0
        child_ptr = 1
        # use slow and fast ptr to assgin child nodes to parents
        while child_ptr < len(b_tree):
            if b_tree[parent_ptr] is not None:
                b_tree[parent_ptr].left = b_tree[child_ptr]
                b_tree[parent_ptr].right = b_tree[child_ptr+1]
                # only when parent node is not None, it will have children 
                # this is why child_ptr += 2 happens in the condition 
                # whereas parent_ptr += 1 happens outside the condition
                child_ptr = child_ptr + 2
            parent_ptr = parent_ptr+1
            
        return b_tree[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))