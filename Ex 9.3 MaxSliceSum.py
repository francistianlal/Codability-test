# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:25:17 2020
simple question

@author: frank
"""
import unittest

N_range = range(1,int(1e6+1))
Element_range = range(-1000000,1000001)

def solution(A):
    end_max = 0
    max_slice = min(Element_range)
    for number in A:
        end_max = max(0,end_max+number)
        max_slice = max(end_max,max_slice)
    if max_slice == 0 and max(A) < 0:
        return max(A)
    return max_slice

class testsolution(unittest.TestCase):
    def test_1(self):
        A=[3,2,-6,4,0]
        self.assertEqual(solution(A),5)

if __name__ == "__main__":
    unittest.main()



