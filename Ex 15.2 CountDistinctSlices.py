# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:12:11 2020

@author: frank
"""

import unittest
N_range = range(1,int(1e5+1))

def solution(M, A):
    count = 0
    front = back = 0
    seen = [False] * (M+1)
    while (front < len(A) and back < len(A)):
        while (front < len(A) and seen[A[front]] != True):
            count += (front-back+1)
            seen[A[front]] = True
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen[A[back]] = False
                back += 1
                 
            seen[A[back]] = False
            back += 1
            
    return min(count, int(1e9))  
    
    
    
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [3,4,5,5,2]
        M = 6
        self.assertEqual(solution(M,A),9)
  
if __name__ == "__main__":
    unittest.main()

