# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:56:42 2020
Frog jump

first attempt only 18% performance.
the problem is asking to find the first point where a array from 1 to X can be found from previous numbers
remember use A in B or A not in B is O(N) time complexity, use dictionary so that the array can be expanded without sorting.
@author: frank
"""
import unittest
NX_range = range(1,int(1e5+1))
def solution(X,A):
    ref = dict()
    for index,number in enumerate(A):
        ref[number] = 1
        if len(ref) == X:
            return index
    return -1
        

class testsolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(5,[1,3,1,4,2,3,5,4]), 6)

    def test_2(self):
        self.assertEqual(solution(6,[1,3,1,4,2,3,5,4]), -1)

    def test_3(self):
        self.assertEqual(solution(5,[1,3,1,5,2,3,5,4]), 7)

    def test_4(self):
        self.assertEqual(solution(2,[2]), -1)

if __name__ == '__main__':    
    unittest.main()


            