# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:11:43 2020
the maximum must appear at the edge of the sorted array,
need to consider both end as negative number is in here
@author: frank
"""

import unittest

N_range = range(3,int(1e5+1))
Element_range = range(int(-1e3),int(1e3+1))

def solution(A):
    A.sort()
    A_max_1 = A[0] * A[1] * A[-1]
    A_max_2 = A[-1] *A[-2] * A[-3]
    if A_max_1 > A_max_2:
        return A_max_1
    return A_max_2

    
class solution_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([-3,1,2,-2,5,6]),60)
    
if __name__ == '__main__':
    unittest.main()