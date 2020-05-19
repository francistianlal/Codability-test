# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:11:48 2020
This is a tricky question.

@author: frank
"""
import unittest
N_range = range(1,int(1e5+1))

def solution(H):
    # the stack can only contain an increasing chain of height
    stack = [H[0]]
    count = 0
    for height in H[1:]:
        while len(stack) != 0 and height < stack[-1]:
            stack.pop()
            count += 1
            # if the height is less than the last block in stack, all blocks that 
            # is smaller than current height can not be combined with blocks coming in the
            # future and thus should be poped out
            # if the new block is the same as any of the previous block, then the higher block will be
            # pop and added to total count and the new block will not be added to the count

        if len(stack) == 0 or height > stack[-1]:
            stack.append(height)
            # if the height can maintain an increasing trend in 
            # the stack it should be kept
            # if the new block is the same as any of the previous block, the higher 
    count += len(stack)
    return count
    
class testsolution(unittest.TestCase):
    def test_1(self):
        H=[8,8,5,7,9,8,7,4,8]
        self.assertEqual(solution(H),7)

if __name__ == "__main__":
    unittest.main()