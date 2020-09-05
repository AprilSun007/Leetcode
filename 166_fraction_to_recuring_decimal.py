#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:22:59 2020

@author: jinwensun
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        num =  numerator
        den = denominator
        
        if den == 0:
            return ''
        if num == 0:
            return "0"
        
        res = []
        if (den < 0) ^ (num < 0):
            res.append('-')
            
        den = abs(den)
        num = abs(num)
        res.append(str(num // den))
        
        if num % den == 0:
            return ''.join(res)
        
        res.append('.')
        rem = num % den
        div_dict = dict()
        
        while(rem != 0):
            if rem in div_dict:
                res.insert(div_dict[rem], '(')
                res.append(')')
                break
            
            div_dict[rem] = len(res)
            n, rem = divmod(rem*10, den)                       
            res.append(str(n))  
            
        return ''.join(res)
        
            
if __name__ == '__main__':
    
    n1 = 4
    n2 = 333
    s = Solution()
    print(s.fractionToDecimal(n1, n2))