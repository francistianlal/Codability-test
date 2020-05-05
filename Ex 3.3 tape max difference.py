# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:32:33 2020
tape difference problem

simple question just remenber to set guard for te last number

@author: frank
"""
import unittest


N_range = range(2,int(1e5+1))
Element_range = range(-1000,1000+1)

def solution(A):

    Sum_A = sum(A)
    count = 0
    Min_count = None
    for number in A[:-1]:
        count += number
        tape = abs(Sum_A - count * 2)
        if Min_count == None:
            Min_count = tape
        if (Min_count) > tape:
            (Min_count) = tape
    return Min_count

class solutiontest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([3,1,2,4,3]),1)

    def test_2(self):
        self.assertEqual(solution([-1000,1000]),2000)

    def test_3(self):
        self.assertEqual(solution([20,0]),20)

if __name__ == '__main__':
    unittest.main()
    
        
        

        
        