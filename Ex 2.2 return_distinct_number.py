# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:05:09 2020
give an array A of N number, return the value of unpaired element
@author: frank
"""
import unittest

N_range = range(1,int(1e6)+1)
Element_range = range(1,int(1e9)+1)

def solution(A):
    N = len(A)
    # set guard for even number length array
    if N % 2 == 0:
        raise ValueError('The array length should be odd')
    # create a dict for reference
    ref = dict()
    for number in A:
        if number not in ref:
            ref[number] = 1
        else:
            ref[number] += 1
    for key in ref:
        if ref[key] % 2 == 1:
            return key

class testsolution(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(solution([9,3,9,3,9,7,9]), 7)

if __name__ == '__main__':
    unittest.main()
