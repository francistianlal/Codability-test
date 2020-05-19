# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:26:55 2020

@author: frank
"""
import unittest

N_range = range(1,int(2149483647))

def solution(N):
    
    def divisor(n):
        i = 1
        result = 0
        while i * i < int(n):
            if n % i == 0:
                result += 2
            i += 1
        if i * i == int(n):
            result += 1
        return result
    
    result = divisor(N)
    return result  

    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = 24
        self.assertEqual(solution(A),8)

    def test_2(self):
        A = 1
        self.assertEqual(solution(A),1)

if __name__ == "__main__":
    unittest.main()


