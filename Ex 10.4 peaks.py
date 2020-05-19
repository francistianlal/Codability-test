# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:02:14 2020

@author: frank
"""
import unittest

N_range = range(1,int(1e5+1))

def solution(A):
    from math import sqrt
    A_len = len(A)
    peaks_until_here = [0]*A_len
    # Retrieve how many peaks exist from beginning to current
    # position.
    for index in range(1, A_len-1):
        peaks_until_here[index] = peaks_until_here[index-1]
        if A[index] > A[index-1] and A[index] > A[index+1]:
            peaks_until_here[index] += 1
    if A_len < 3 or peaks_until_here[-2] == 0:
        # The array is too short to have a peak. OR
        # There is no peak in this array.
        return 0
    peaks_until_here[-1] = peaks_until_here[-2]
    max_blocks = 0
    # Compute every possible partition plan, and find out the
    # one with most blocks.
    for candidate in range(1, int(sqrt(A_len))+1, 1):
        if A_len % candidate == 0:
            blocks, block_size = candidate, A_len//candidate
            # Check the first block.
            if peaks_until_here[0] < peaks_until_here[block_size-1]:
                # Check the following blocks.
                for each_block in range(block_size, A_len, block_size):
                    if peaks_until_here[each_block-1] == \
                       peaks_until_here[each_block+block_size-1]:
                        # No peak is found in the next block
                        # This partition plan is not accepted
                        break
                else:
                    max_blocks = blocks
            if candidate * candidate == A_len:
                # If candidate is equal to sqrt(A_len) exactly,
                # candidate would equal to A_len//candidate.
                continue
            block_size, blocks = candidate, A_len//candidate
            # Check the first block.
            if peaks_until_here[0] < peaks_until_here[block_size-1]:
                # Check the following blocks.
                for each_block in range(block_size, A_len, block_size):
                    if peaks_until_here[each_block-1] == \
                       peaks_until_here[each_block+block_size-1]:
                        # No peak is found in the next block
                        # This partition plan is not accepted
                        break
                else:
                    return blocks
    return max_blocks

class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,2,3,4,3,4,1,2,3,4,6,2]
        self.assertEqual(solution(A),3)

if __name__ == "__main__":
    unittest.main()
