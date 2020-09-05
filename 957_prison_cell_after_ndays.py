#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:32:24 2020

@author: jinwensun
"""

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        seen = dict()
        
        n = 0
        repeat = False
        while n < N:
            if tuple(cells) in seen:
                repeat = True
                break
                                
            else:
                seen[tuple(cells)] = n
                cells = self.next_state(cells)                         
                n += 1
        if repeat:
            step = n - seen[tuple(cells)]
            rem = (N - seen[tuple(cells)])%step
            
            for i in range(rem):
                cells = self.next_state(cells)
            
        return cells
        
    def next_state(self, cells):
        c = []
        for i in range(len(cells)):           
            if i == 0:
                c.append(0)
            elif i == len(cells) - 1:
                c.append(0)
            else:
                if cells[i-1] == cells[i+1]:
                    c.append(1)
                else:
                    c.append(0)
                                 
        return c
    
if __name__ == '__main__':
    s = Solution()
    cells = [0,1,0,1,1,0,0,1]
    N = 7
    
    print(s.prisonAfterNDays(cells, N))
