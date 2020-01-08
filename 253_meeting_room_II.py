#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:35:54 2020

@author: jinwensun

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        if len(intervals) == 0:
            return 0
        
        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        
        meeting_rooms = []
        for idx, interval in enumerate(sorted_intervals):
            if idx == 0:
                meeting_rooms.append(interval[1])
            else:
                strt_time = interval[0]
                end_time = interval[1]
                if strt_time >= min(meeting_rooms):
                    _ = heapq.heappushpop(meeting_rooms, end_time)
                else:
                    heapq.heappush(meeting_rooms, end_time)
                    
        return len(meeting_rooms)
    

if __name__ == '__main__':
    nums = [[0, 30],[5, 10],[15, 20]]
    s = Solution()
    print(s.minMeetingRooms(nums))       
        
                    
                    
                
            