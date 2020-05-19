# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:42:08 2020
This question is the simplied version of Ex 7.1
@author: frank
"""
import unittest

def solution(S):
    match = {"(":")"}
    if len(S) % 2 == 1:
        return 0
    stack = []
    for letter in S:
        if letter == "(":
            stack.append(letter)
        else:
            if len(stack) == 0:
                return 0
            elif match[stack.pop()] != letter:
                return 0
    if len(stack) == 0:
        return 1
    return 0
                
    
class testsolution(unittest.TestCase):
    def test_1(self):
        S = "(()(())())"
        self.assertEqual(solution(S),1)

    def test_2(self):
        S = "())"
        self.assertEqual(solution(S),0)

if __name__ == "__main__":
    unittest.main()