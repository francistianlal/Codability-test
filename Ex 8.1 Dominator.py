# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:44:19 2020
Remeber dominator needs more than half occurence
if len(A) is odd, the number of occurence needed is len(A)//2+1
@author: frank
"""
import unittest
import random
N_range = range(0,int(1e5+1))

def solution(A):
    Position = []
    stack = []
    for number in A:
        if len(stack) == 0 or stack[-1] == number:
            stack.append(number)
        elif stack[-1] != number:
            stack.pop()
    if len(stack) == 0:
        return -1
    if len(stack) > 0:
        candidate = stack[-1]
        count = 0
    for index,number in enumerate(A):
        if number == candidate:
            Position.append(index)
            count += 1
    if count > len(A) // 2:
        return random.choice(Position)
    return -1
        
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A=[3,4,3,2,3,-1,3,3]
        Position = [0,2,4,6,7]
        self.assertIn(solution(A),Position)

if __name__ == "__main__":
    unittest.main()
