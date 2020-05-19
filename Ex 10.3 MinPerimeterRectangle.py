# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:16:59 2020
too simple
@author: frank
"""
import unittest
import math
N_range = range(1,int(1e9+1))

def solution(N):
    # Basically find the devisor that approach the sqrt(N)
    N_sqrt = round(math.sqrt(N))
    for number in reversed(range(1,N_sqrt+1)):
        if N % number == 0:
            perimeter = 2 * (number + N / number)
            return int(perimeter) 
        
    

    
class testsolution(unittest.TestCase):
    def test_1(self):
        N = 30
        self.assertEqual(solution(N),22)

    def test_2(self):
        N = 1
        self.assertEqual(solution(N),4)

if __name__ == "__main__":
    unittest.main()