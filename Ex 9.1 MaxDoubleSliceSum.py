# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:50:41 2020
First use the max slice function, remember to pop out the two number on the edge when input matrix
Solution come from https://www.martinkysel.com/codility-maxdoubleslicesum-solution/
@author: frank
"""

import unittest

N_range = range(3,int(1e5+1))


def solution(A):
    ending_here = [0] * len(A)
    starting_here = [0] * len(A)
     
    for idx in range(1, len(A)):
        ending_here[idx] = max(0, ending_here[idx-1] + A[idx])
     
    for idx in reversed(range(len(A)-1)):
        starting_here[idx] = max(0, starting_here[idx+1] + A[idx])
     
    max_double_slice = 0
     
    for idx in range(1, len(A)-1):
        max_double_slice = max(max_double_slice, starting_here[idx+1] + ending_here[idx-1])
         
         
    return max_double_slice

class testsolution(unittest.TestCase):
    def test_1(self):
        A=[3,2,6,-1,4,5,-1,2]
        self.assertEqual(solution(A),17)

    def test_2(self):
        A=[3,3,3]
        self.assertEqual(solution(A),0)

    def test_3(self):
        A=[0, 10, -5, -2, 0]
        self.assertEqual(solution(A),10)
        
    def test_4(self):
        A=[-10,-2,-23,-2]
        self.assertEqual(solution(A),0)

    def test_5(self):
        A=[-8, 10, 20, -5, -7, -4]
        self.assertEqual(solution(A),30)

if __name__ == "__main__":
    unittest.main()

