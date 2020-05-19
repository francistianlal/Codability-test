# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:02:42 2020
Too easy 

@author: frank
"""
import unittest

N_range = range(1,int(1e5+1))
A_range = range(0,int(1e9+1))


def solution(A, B):
    big_dog = []
    count = 0
    index = 0
    while index < len(A):
        if B[index] == 1:
            big_dog.append(A[index])
        else:
            if len(big_dog) == 0:    
                count += 1
            elif big_dog[-1] < A[index]:
                big_dog.pop()
                index -= 1
        index += 1
    count += len(big_dog)
    return count
                
            
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [4,3,2,1,5]
        B = [0,1,0,0,0]
        self.assertEqual(solution(A,B),2)

if __name__ == "__main__":
    unittest.main()