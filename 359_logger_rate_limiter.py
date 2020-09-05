#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:08:53 2020

@author: jinwensun
"""

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.msg_dict = dict() # msg: last_print_time_stamp
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.msg_dict:
            pst_ts = self.msg_dict[message]
            if timestamp - pst_ts >= 10:
                self.msg_dict[message] = timestamp
                return True
            else:
                return False
        
        else:
            self.msg_dict[message] = timestamp
            return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)