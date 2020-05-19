# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:35:35 2020
basic queue structrue should work
remember to set the guard to sign only
remember only pop and push the 0th and -1th element
remember to check if the size of input is even
@author: frank
"""
import unittest

N_range = range(0,int(2e5+1))
Element_range = "[]{}()"

def solution(A):
    # check if the size is even
    if len(A) % 2 == 1:
        return 0
    # define a function for checking pairing
    match = {"[":"]","{":"}","(":")"}
    stack = []
    start_sign =["[","(","{"]
    for letter in A:
        if letter in start_sign:
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
        self.assertEqual(solution(A = "{[()()]}"),1)

    def test_2(self):
        self.assertEqual(solution(A = "([)()]"),0)

    def test_3(self):
        self.assertEqual(solution(A = ""),1)

    def test_4(self):
        self.assertEqual(solution(A = "[44e]"),0)

    def test_5(self):
        self.assertEqual(solution(A = ")("),0)

if __name__ == "__main__":
    unittest.main()