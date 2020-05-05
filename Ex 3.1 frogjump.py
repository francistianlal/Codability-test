# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:16:37 2020
Frog jump problem

@author: frank
"""
import unittest

Element_range = range(1,int(1e9+1))

def solution(X,Y,D):
    if X not in Element_range or Y not in Element_range or D not in Element_range :
        raise TypeError('element not in range')
    if X > Y:
        raise ValueError('X should be smaller than Y')
    if (Y-X) % D != 0:
        return (Y-X)//D + 1
    return (Y-X)//D

class testsolution(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(solution(10,85,30),3)

if __name__ == '__main__':
    unittest.main()