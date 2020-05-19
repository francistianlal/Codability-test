# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:20:36 2020

@author: frank
"""
import unittest
N_range = range(1,int(1e5+1))

def solution(K,A):
    count = 0
    current_length = 0
    for number in A:
        current_length += number
        if current_length >= K:
            current_length = 0 
            count += 1
    return count
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,2,3,4,1,1,3]
        K = 4
        self.assertEqual(solution(K,A),3)

if __name__ == "__main__":
    unittest.main()



