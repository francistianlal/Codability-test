# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:50:03 2020
too simple

@author: frank
"""
import unittest

N_range = range(0,int(1e5+1))
Element_range = range(int(-1e6),int(1e6+1))

def solution(A):
    ref = {}
    for number in A:
        ref[number] = 1
    return len(ref)


    
class solution_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([2,1,1,2,3,1]),3)
    
if __name__ == '__main__':
    unittest.main()