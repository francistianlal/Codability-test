# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:38:31 2020
return the missing number.

I got almost everything wrong at first, this is not really a simple question
1. did not consider the case with single element input
2. did not set guard that the array have nothing missing
3. didn't consider empty matrix, N = 0
if you get everything right still only 60% score due to the time complexity
avoid using sort method and detect the missing number index by calculating difference
can not write guard code in this txt
@author: frank
"""
import unittest

N_range = range(1,int(1e5)+1)

def solution(A):
    N = len(A)

    if N == 0:
        return 1
    return int(-(sum(A) - (2+N)*(N+1)/2))

class testsolution(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(solution([2,3,1,5]),4)
        
    def test_2(self):
        self.assertEqual(solution([2]),1)
          
    def test_3(self):
        self.assertEqual(solution([1,2]),3)

    def test_4(self):
        self.assertEqual(solution([]),1)

    def test_5(self):
        self.assertEqual(solution([2,3]),1)

    def test_6(self):
        self.assertEqual(solution([2]),1)

    def test_7(self):
        self.assertEqual(solution([1,3]),2)
if __name__ == '__main__':
    unittest.main()
  