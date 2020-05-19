# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:39:07 2020
Not difficult but need to set a lot of guard, remember one element can 
be extract twice
@author: frank
"""
import unittest
N_range = range(1,int(1e5+1))

def solution(A):
    
    A.sort()
    lower = 0
    upper = len(A) - 1
    minimum = int(3e9)
    
    if min(A) >= 0 and len(A) > 1:
        return 2 * A[0]
    if max(A) <= 0 and len(A) > 1:
        return abs(2 * A[-1])

    
    while lower <= upper:
        if minimum == 0:
            return 0
        minimum = min(minimum, abs(A[upper]+A[lower]))
        if abs(A[upper]) > abs(A[lower]):
            upper -= 1
        else:
            lower += 1
    return minimum
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [-8,4,5,-10,3]
        self.assertEqual(solution(A),3)

    def test_2(self):
        A = [1,4,-3]
        self.assertEqual(solution(A),1)

    def test_3(self):
        A = [1000000000]
        self.assertEqual(solution(A),2000000000)

    def test_4(self):
        A = [0]
        self.assertEqual(solution(A),0)

    def test_5(self):
        A = [8, 5, 3, 4, 6, 8]
        self.assertEqual(solution(A),6)
  
if __name__ == "__main__":
    unittest.main()


