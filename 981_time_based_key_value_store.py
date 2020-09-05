#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:33:44 2020

@author: jinwensun
"""

import bisect
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.timestamp = dict()
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.data:            
            self.data[key] = {timestamp:value}
            self.timestamp[key] = [timestamp]
        else:
            self.data[key][timestamp] = value
            self.timestamp[key].append(timestamp)
            
            
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.data:
            return ""
        
        i = bisect.bisect(self.timestamp[key], timestamp)
        if i == 0:
            return ""
                   
        return self.data[key][self.timestamp[key][i-1]]
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)