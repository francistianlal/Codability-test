# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:20:22 2020

@author: frank
"""

import unittest
N_range = range(1,int(1e5+1))


def solution(A):
    A = [abs(item) for item in A]
    sumOfA = sum(A)
    numbers = {}
    for item in A:  
        numbers[item] = numbers.get(item, 0) + 1
    possible = [-1] * (sumOfA // 2 + 1)
    possible[0] = 0
    for number in numbers:   
        for trying in range(sumOfA//2+1):
            if possible[trying] >= 0:
                possible[trying] = numbers[number]
            elif trying >= number and possible[trying-number] > 0:
                 possible[trying] = possible[trying-number] - 1
   
    for halfSum in range(sumOfA//2, -1, -1):
        if possible[halfSum] >= 0:
            return sumOfA - halfSum - halfSum
    raise Exception("Should never be here!")
    return 0

class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,5,2,-2]
        self.assertEqual(solution(A),0)

    def test_2(self):
        A = []
        self.assertEqual(solution(A),0)

    def test_3(self):
        A = [3, 3, 3, 4, 5]
        self.assertEqual(solution(A),0)

    def test_4(self):
        A = [1, 5, -2, 5, 2, 3]
        self.assertEqual(solution(A),0)

if __name__ == "__main__":
    unittest.main()
