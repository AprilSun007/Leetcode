#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:36:48 2020

@author: jinwensun
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        board_dict = dict()
        box_dict = dict()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    
                    if (i//3, j//3) in box_dict:
                        if board[i][j] in box_dict[(i//3, j//3)]:
                            return False
                        box_dict[(i//3, j//3)].add(board[i][j])
                        
                    else:
                        box_dict[(i//3, j//3)] = {board[i][j]}
                                       
                    if board[i][j] in board_dict:
                        if i in board_dict[board[i][j]][0]:
                            return False
                        if j in board_dict[board[i][j]][1]:
                            return False
                        board_dict[board[i][j]][0].add(i)
                        board_dict[board[i][j]][1].add(j)                    
                    
                    else:
                        board_dict[board[i][j]] = [{i}, {j}]
                        
        return True
                        
                        
        
            
                    
                
        
                        
                        
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.isValidSudoku(board))

