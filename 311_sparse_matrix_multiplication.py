#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:01:18 2020

@author: jinwensun
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if A is None or B is None or len(A) == 0 or len(B) == 0:
            return None
        
        a_dict = self.sparse_matrix_rep(A, axis = 0)
        b_dict = self.sparse_matrix_rep(B, axis = 1)
        
        n_row_A = len(A)
        n_col_A = len(A[0])
        n_col_B = len(B[0])
        
        result = [ [0 for i in range(n_col_B)] for i in range(n_row_A)]
        
        for i in range(n_row_A):
            r = 0
            for j in range(n_col_B):
                for z in range(n_col_A):
                    if z in a_dict[i] and z in b_dict[j]:
                        r += a_dict[i][z]* b_dict[j][z]
                        
                result[i][j] = r
        return result        
         
    def sparse_matrix_rep(self, A, axis = 0):
        if A is None or len(A) == 0:
            return None
        
        a_dict = dict()
        if axis == 0:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    #processA[i][j]

                    if i not in a_dict:
                        a_dict[i] = dict()
                    
                    if A[i][j] == 0:
                        continue

                    a_dict[i][j] = A[i][j]
                    
        if axis == 1:            
            for j in range(len(A[0])):
                for i in range(len(A)):
                    #processA[i][j]

                    if j not in a_dict:
                        a_dict[j] = dict()
                        
                    if A[i][j] == 0:
                        continue

                    a_dict[j][i] = A[i][j]
            
            
        return a_dict
        
if __name__ == '__main__':
    A = [[1,0,0],[-1,0,3]]
    B = [[7,0,0],[0,0,0],[0,0,1]]
    
    s = Solution()
    print(s.multiply(A, B))
    
    
    
    
    