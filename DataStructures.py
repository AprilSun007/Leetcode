#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:47:08 2019

@author: jinwensun
"""

class LinkedList:
    def __init__(self,node ):
        self.head = node
        self.next = None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
     
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_value(self, value):
        self.value = value
    
    def set_next(self, value):
        self.next = value
        
    def delete_next(self):
        self.next = None
        