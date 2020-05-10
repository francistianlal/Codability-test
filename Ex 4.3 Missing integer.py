# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:10:50 2020
Missing integer

this one is too easy

@author: frank
"""
import unittest

N_range = range(1,int(1e5+1))


def solution(A):
    A.sort()
    ref = 0 
    for number in A:
        if number <= 0:
            continue
        elif number > 0:
            if number == ref:
                continue
            if number == ref + 1:
                ref += 1
            if number != ref:
                return ref+1
    return ref+1

class testsolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1,3,6,4,1,2]), 5)

    def test_2(self):
        self.assertEqual(solution([1,2,3]), 4)

    def test_3(self):
        self.assertEqual(solution([-1,-3]), 1)

if __name__ == '__main__':
    unittest.main()