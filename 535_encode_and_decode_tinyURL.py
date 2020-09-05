#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:08:47 2020

@author: jinwensun
"""

class Codec:
    table = dict()
    cnt = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
      
        self.cnt += 1
        self.table[str(self.cnt)] = longUrl 
        
        return "http://tinyurl.com/" + str(self.cnt)
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.table[shortUrl[len('http://tinyurl.com/'):]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))