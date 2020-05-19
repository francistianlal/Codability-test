# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:24:58 2020

@author: frank
"""
import unittest

N_range = range(0,int(4e5+1))


def solution(A):
    # convert A to loss and gain array
    GL = []
    end_max = 0
    profit_max = -1 
    for index in range(1,len(A)):
        GL.append(A[index]-A[index-1])
    for number in GL:
        end_max = max(0,end_max+number)
        profit_max = max(profit_max,end_max) 
    if profit_max < 0:
        return 0
    return profit_max
        
class testsolution(unittest.TestCase):
    def test_1(self):
        A=[23171,21011,21123,21366,21013,21367]
        self.assertEqual(solution(A),356)

if __name__ == "__main__":
    unittest.main()

