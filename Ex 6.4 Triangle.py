# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:18:10 2020
too simple
@author: frank
"""
import unittest

N_range = range(0,int(1e5+1))
Element_range = range(int(-2147483648),int(2147483647+1))

def solution(A):
    A.sort()
    if len(A) < 3:
        return 0

    for number in range(0,len(A)-2):
        if A[number] + A[number + 1] > A[number + 2]:
            return 1
    return 0




class solution_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([10,2,5,1,8,20]),1)
    
    def test_2(self):
        self.assertEqual(solution([10,50,5,1]),0)

    def test_4(self):
        self.assertEqual(solution([0,0,1]),0)
                
if __name__ == '__main__':
    unittest.main()

