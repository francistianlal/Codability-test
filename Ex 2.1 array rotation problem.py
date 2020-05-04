# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:45:27 2020
array rotation to the right
rotate the array of length N by K
@author: frank
"""
import unittest

NK_range = range(0, 100+1)
Element_range = range(-1000,1000+1)

def solution(A, K):
    N = len(A)
    A_new = list()
    for index,number in enumerate(A):
        index_new = (index - K) % N
        A_new.append(A[index_new])
    return A_new

class testsolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([3,8,9,7,6],3), [9,7,6,3,8])

    def test_2(self):
        self.assertEqual(solution([0,0,0],1), [0,0,0])

    def test_3(self):
        self.assertEqual(solution([1,2,3,4],4), [1,2,3,4])

if __name__ == '__main__':
    unittest.main()