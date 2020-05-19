# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:47:00 2020

@author: frank
"""
import unittest
NM_range = range(1,int(1e5+1))

def solution(A):
    ref = {}
    for number in A:
        number = abs(number)
        if number not in ref:
            ref[number] = 1
    
    return len(ref)
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [-5,-3,-1,0,3,6]
        self.assertEqual(solution(A),5)
  
if __name__ == "__main__":
    unittest.main()



