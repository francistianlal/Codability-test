# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:45:06 2020
This is a really difficult question
Solution come from others
@author: frank
"""
import unittest

N_range = range(1,int(4e5+1))

from math import sqrt

def transform(A):
    peak_pos = len(A)
    last_height = A[-1]
    for p in range(len(A) - 1, 0, -1):
        if (A[p - 1] < A[p] > last_height):
            peak_pos = p
        last_height = A[p]
        A[p] = peak_pos
    A[0] = peak_pos

    
def can_fit_flags(A, k):
    flag = 1 - k
    for i in range(k):
        # plant the next flag at A[flag + k]
        if flag + k > len(A) - 1:
            return False
        flag = A[flag + k]
    return flag < len(A)  # last flag planted successfully

def solution(A):
    transform(A)
    lower = 0
    upper = int(sqrt(len(A))) + 2
    assert not can_fit_flags(A, k=upper)
    while lower < upper - 1:
        next = (lower + upper) // 2
        if can_fit_flags(A, k=next):
            lower = next
        else:
            upper = next
    return lower
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,5,3,4,3,4,1,2,3,4,6,2]
        self.assertEqual(solution(A),3)


if __name__ == "__main__":
    unittest.main()
