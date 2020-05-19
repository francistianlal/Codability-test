# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:03:44 2020

@author: frank
"""
import unittest
N_range = range(0,int(3e4+1))

def solution(A,B):
    
    len_current = 1
    if len(A) <= 1:
        return len(A)
    
    last = B[0]
    index = 1
    while index < len(A):
        if A[index] > last:
            len_current += 1
            last = B[index]
        index += 1
    return len_current
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,3,7,9,9]
        B = [5,6,8,9,10]
        self.assertEqual(solution(A,B),3)

    def test_2(self):
        A = []
        B = []
        self.assertEqual(solution(A,B),0)

    def test_3(self):
        A = [0, 2, 100]
        B = [0, 50, 1000]
        self.assertEqual(solution(A,B),3)
if __name__ == "__main__":
    unittest.main()


