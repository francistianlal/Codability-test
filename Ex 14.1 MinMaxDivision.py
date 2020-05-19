# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:44:52 2020
M is complete useless
@author: frank
"""
import unittest
NK_range = range(1,int(1e5+1))
M_range =  range(0,int(1e4))

def solution(K, M, A):
    # build a function to check if the solve is true
    def solve_check(A,K,candidate):
        current_block_sum = 0
        block_count = 1
        for number in A:
            if current_block_sum + number > candidate:
                block_count += 1
                current_block_sum = number
            else:
                current_block_sum += number
                
            if block_count > K:
                return False
        return True
                
    max_block = sum(A)
    min_block = max(A)
    # if the number of blocks are greater than the size of A, then we have min_block
    if len(A) < K:
        return min_block
    if K == 1:
        return max_block
    
    while min_block <= max_block:
        candidate = (max_block + min_block) // 2
        if solve_check(A,K,candidate):
            max_block = candidate - 1
        else:
            min_block = candidate + 1
    return min_block
        
class testsolution(unittest.TestCase):
    def test_1(self):
        K = 3
        M = 5
        A = [2,1,5,1,2,2,2]
        self.assertEqual(solution(K,M,A),6)
  
if __name__ == "__main__":
    unittest.main()

