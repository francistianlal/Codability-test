# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:43:43 2020
Maxcounter problem

The trick in this questions is to update the min and max level of the counter
the second operation will need to extract the max number from counter and update every number in the coutter
this increase the time complexity
@author: frank
"""
import unittest

NM_range = range(1,int(1e5+1))

def solution(N,A):
    min_level = 0
    max_level = 0 
    counter = [0] * N
    for number in A:
        if number <1 or number >N+1:
            raise ValueError('the element is not in range')
        if number <=N:
            if counter[number-1] < min_level:
                counter[number-1] = min_level
            counter[number-1] +=1
            if max_level < counter[number-1]:
                max_level = counter[number-1]
        else:
            min_level = max_level
     
    for index,number in enumerate(counter) :
        if number < min_level:
            counter[index] = min_level
    return counter


                
class testsolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(5,[3,4,4,6,1,4,4]), [3,2,2,4,2])

if __name__ == '__main__':
    unittest.main()