#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:36:14 2020

@author: jinwensun
"""

import heapq
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        
        grade_dict = dict()
        
        for item in items:
            student_id = item[0]
            student_grade = item[1]
            
            if student_id in grade_dict:
                heapq.heappush(grade_dict[student_id], student_grade)            
            else:
                grade_dict[student_id] = [student_grade]
                heapq.heapify(grade_dict[student_id])
            
        result = list()
        for key, value in grade_dict.items():
            result.append([key, sum(heapq.nlargest(5, value))/5])
        
        return result
    
if __name__ == '__main__':
    
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    
    s = Solution()
    print(s.highFive(items))