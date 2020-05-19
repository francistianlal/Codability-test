# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:47:27 2020

@author: frank
"""
import unittest
L_range = range(1,int(5e4+1))

def solution(A, B):
    L = max(A)
    P_max = max(B)
  
    fib = [0] * (L+2)
    fib[1] = 1
    for i in range(2, L + 2):
        fib[i] = (fib[i-1] + fib[i-2]) & ((1 << P_max) - 1)
  
    return_arr = [0] * len(A)
  
    for idx in range(len(A)):
        return_arr[idx] = fib[A[idx]+1] & ((1 << B[idx]) - 1)
  
    return return_arr

class testsolution(unittest.TestCase):
    def test_1(self):
        A = [4,4,5,5,1]
        B = [3,2,4,3,1]
        self.assertEqual(solution(A,B),[5,1,8,0,1])

if __name__ == "__main__":
    unittest.main()