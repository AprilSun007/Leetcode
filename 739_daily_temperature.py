#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:10:48 2020

@author: jinwensun
"""

from collections import defaultdict
class Solution_0(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        temp_dict = defaultdict(list)
        
        for i, t in enumerate(T):
            temp_dict[t].append(i)
            
        result = []
        for i, t in enumerate(T):
            idx_list = []
            for k, v in temp_dict.items():
                if k > t:
                    idx_list += [idx for idx in v if idx > i]
            if len(idx_list) == 0:
                result.append(0)
            else:
                result.append(min(idx_list) - i)
                
        return result
                
    
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        :time complexity: O(N)
        :space complesity: O(W) bounded. because it's strictly increasing, and T in range[30, 100]
        """
        stack = []
        result = [0]*len(T)
        for i in range(len(T) - 1, -1, -1):
            # 对于每个i， stack 存的都是他之后的一个升序的温度
            # 最精巧的是pop了比当前T[i] 低的温度， 因为不需要： 
            #   当你走到比i小的index的时候， 如果那个温度比T[i] 小， 那会考率T[i]， T[i+1] 根本不会被考虑， 
            #                            如果那个温度比T[i]大， 那肯定更比T[i+1]大， T[i+1]也不会被考虑。
            # 这个pop还蛮精巧的
            while len(stack) > 0 and T[i] >= T[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                result[i] = stack[-1] - i
            stack.append(i)
        return result
     