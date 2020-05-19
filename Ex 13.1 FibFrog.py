# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:03:38 2020
from https://www.martinkysel.com/codility-fibfrog-solution/
@author: frank
"""
import os
cwd = os.getcwd() 
print(cwd)
os.chdir('C:/Users/frank/.spyder-py3/practical example/codability/')

import unittest
Z_range = range(1,int(6e3+1))

def solution(A):
    
    Step_total = len(A) + 2
    
    def fibonacci(n):
       fib = []
       fib.append(0)
       fib.append(1)
       i = 2
       fib_new = 2
       while fib_new < n:
           fib_new = fib[i-1] + fib[i-2]
           fib.append(fib_new)
           i += 1
       return fib[1:-1]   
   
    fib_set = fibonacci(Step_total)
    A.append(1)
      
    # this array will hold the optimal jump count that reaches this index
    reachable = [-1] * (len(A))
     
    # get the leafs that can be reached from the starting shore
    for jump in fib_set:
        if A[jump-1] == 1:
            reachable[jump-1] = 1
     
    for idx in range(len(A)):
        # ignore non-leafs and already found paths
        if A[idx] == 0 or reachable[idx] > 0:
            continue
 
        # get the optimal jump count to reach this leaf
        min_idx = -1
        min_value = 100000
        for jump in fib_set:
            previous_idx = idx - jump
            if previous_idx < 0:
                break
            if reachable[previous_idx] > 0 and min_value > reachable[previous_idx]:
                min_value = reachable[previous_idx]
                min_idx = previous_idx
        if min_idx != -1:
            reachable[idx] = min_value +1
    
    return reachable[-1]

class testsolution(unittest.TestCase):
    def test_1(self):
        A = [0,0,0,1,1,0,1,0,0,0,0]
        self.assertEqual(solution(A),3)

    def test_2(self):
        A = []
        self.assertEqual(solution(A),-1)

if __name__ == "__main__":
    unittest.main()