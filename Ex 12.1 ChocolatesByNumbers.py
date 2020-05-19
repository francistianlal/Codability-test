# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:26:48 2020
find the least common multiply
@author: frank
"""
import unittest
N_range = range(1,int(1e9+1))

def solution(N,M):
    
    def gcd(N,M):
        if N % M ==0:
            return M
        else:
            return gcd(M,N % M)
    
    def lcm(N,M):
        return N * (M / gcd(N,M))
    

    
    return int(lcm(N,M) /M)

class testsolution(unittest.TestCase):
    def test_1(self):
        N = 10
        M = 4
        self.assertEqual(solution(N,M),5)

    def test_2(self):
        N = 947853
        M = 4453
        self.assertEqual(solution(N,M),947853)

if __name__ == "__main__":
    unittest.main()
    