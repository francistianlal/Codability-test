# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:05:44 2020

@author: frank
"""
import unittest
N_range = range(1,int(1e5+1))

def solution(A):
    A.sort()
    triangle_cnt = 0
     
    for P_idx in range(0, len(A)-2):
        Q_idx = P_idx + 1
        R_idx = P_idx + 2
        while (R_idx < len(A)):
            if A[P_idx] + A[Q_idx] > A[R_idx]:
                triangle_cnt += R_idx - Q_idx
                R_idx += 1
            elif Q_idx < R_idx -1:
                    Q_idx += 1
            else:
                R_idx += 1
                Q_idx += 1
                 
    return triangle_cnt
    
    
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [10,2,5,1,8,12]
        self.assertEqual(solution(A),4)
  
if __name__ == "__main__":
    unittest.main()



