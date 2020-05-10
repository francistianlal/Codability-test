# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:46:19 2020
the smart way of doing this question is calculating
the number of divisible number of A and B, then get the difference
@author: frank
"""
import unittest

AB_range = range(0,int(2e9+1))
K_range = range(1,int(2e9+1))

def solution(A,B,K):
    A_num = A//K
    B_num = B//K
    if A % K == 0:
        return B_num - A_num + 1
    return B_num - A_num

class solutiontest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(6,11,2), 3)

if __name__ == '__main__':
    unittest.main()
    