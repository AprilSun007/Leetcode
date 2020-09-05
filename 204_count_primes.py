#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:08:54 2020

@author: jinwensun
"""
# too slow wont get accepted
class Solution0(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        primes = set()
        primes.add(2)
        
        for i in range(3, n):
            prime_ind = True
            for pm_num in primes:
                if pm_num < i:
                    if i % pm_num ==0:
                        prime_ind = False
                        break
            if prime_ind:
                primes.add(i)
                
        return len(primes)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.sieve_of_eratosthenes(n)
    
    def sieve_of_eratosthenes(self, n):
        # time complexity: nloglog(n) https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
        # I didn't read through
        if n < 3:
            return 0
        
        prime_ind = [True for i in range(n)]
        prime_ind[0] = False
        prime_ind[1] = False
        
        for num in range(2, n):
            if prime_ind[num]:
                multi_num = num + num
                while(multi_num  < n):
                    prime_ind[multi_num] = False
                    multi_num += num
            else:
                continue
                
        return sum(prime_ind)
                
    
    
if __name__ == '__main__':
    s0 = Solution0()
    s = Solution()
    n = 499995
    print(s.countPrimes(n))
    print(s0.countPrimes(n))