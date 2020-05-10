# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:37:40 2020
Very simple question, but need to be careful with
case 3 and 4
@author: frank
"""
import unittest

N_range = range(1,int(1e5+1))


def solution(A):
    A_max = 0
    ref = dict()
    for number in A:
        if number > A_max:
            A_max = number
        ref[number] = 1
    if len(ref) == A_max and len(A) == A_max:
        return 1
    return 0

class solutiontest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(A=[4,1,3,2]), 1)
        
    def test_2(self):
        self.assertEqual(solution([4,1,3]), 0)

    def test_3(self):
        self.assertEqual(solution([3,1,1]), 0)

    def test_4(self):
        self.assertEqual(solution([1,1]), 0)

if __name__ == '__main__':
    unittest.main()

