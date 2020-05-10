# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:22:39 2020
Count the number of 0 appearing before we encounter a 1 or vice versa

also don't run this program with test2 cause you PC will explode
@author: frank
"""
import unittest

def solution(A):
    # we based the count on 1
    counter_0 = 0
    total_pair = 0
    for number in A:
        if number == 0:
            counter_0 += 1
        if number == 1:
            total_pair += counter_0
    if total_pair <= int(1e9):
        return total_pair
    return -1

class testsolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([0,1,0,1,1]), 5)

    def test_1(self):
        self.assertEqual(solution([1]+[0]*int(1e9)), -1)

if __name__ == '__main__':
    unittest.main() 