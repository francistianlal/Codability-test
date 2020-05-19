# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:08:59 2020
Difficult one
@author: frank
"""
import unittest

N_range = range(1,int(5e4+1))

def solution(A):

    def divisor(number):
        n = int(number)    
        i = 1
        divisor = []
        while i*i < n:
            if n % i == 0:
                divisor.append(i)
                divisor.append(int(n/i))
            i += 1
        if i * i == n:
            divisor.append(int(i))
        return (divisor)
    
    ref = {}
    divisor_set ={}
    for number in A:
        if number not in ref:
            divisor_number = divisor(number)
            divisor_set[number] = divisor_number
            ref[number] = 1
        else:
             ref[number] += 1
             
    result = [0] * len(A)
    for idx, element in enumerate(A):
        result[idx] = (len(A)-sum([ref.get(divisor,0) for divisor in divisor_set[element]]))
  
    return result
        
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [3,1,2,3,6]
        self.assertEqual(solution(A),[2,4,3,2,0])

if __name__ == "__main__":
    unittest.main()

