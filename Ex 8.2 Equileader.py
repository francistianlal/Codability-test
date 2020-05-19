# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:11:57 2020
use the module in 8.1 and its pretty simple
@author: frank
"""
import unittest

N_range = range(1,int(1e5+1))
element_range = range(int(-1e9),int(1e9+1))

def solution(A):
    def find_dominator(A):        
        stack = []
        Position = []
        for number in A:
            if len(stack) == 0 or stack[-1] == number:
                stack.append(number)
            elif stack[-1] != number:
                    stack.pop()
        if len(stack) == 0:
                return -1,[]
        if len(stack) > 0:
                candidate = stack[-1]
                count = 0
        for index,number in enumerate(A):
            if number == candidate:
                    Position.append(index)
                    count += 1
        if count > len(A) // 2:
            return candidate,Position
        return -1,[]
    
    candidate,Position = find_dominator(A)
    if candidate == -1:
        return 0
    else:
        equi = 0
        count_to_left = 0
        for index, number in enumerate(A):
            if number == candidate:
                count_to_left += 1
                count_to_right = len(Position) - count_to_left
            if count_to_left > (index+1)//2 and count_to_right > (len(A)-index-1)//2:
                equi += 1
    return equi
class testsolution(unittest.TestCase):
    def test_1(self):
        A=[4,3,4,4,4,2]
        self.assertEqual(solution(A),2)

    def test_2(self):
        A = [4, 4, 2, 5, 3, 4, 4, 4]
        self.assertEqual(solution(A),3)

if __name__ == "__main__":
    unittest.main()

