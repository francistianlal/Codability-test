# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:48:00 2020
The straight forward method will need at least O(N**2) complexity
The length of minimum splice average will not be longer than 3, which we 
can take advantage of
@author: frank
"""
import unittest
Element_range = range(int(-1e5),int(1e5+1))

def solution(A):
    N = len(A)
    min_average = max(Element_range)
    min_average_position = 0
    if N == 2:
        min_average = (A[0] + A[1]) /2
    else:            
        for number in range(0,N-2):
            A_3_avg = (A[number]+A[number+1]+A[number+2])/3
            A_2_avg1 = (A[number]+A[number+1])/2
            A_2_avg2 = (A[number+1]+A[number+2])/2     
            if min(A_3_avg,A_2_avg1) < min_average:
                min_average = min(A_3_avg,A_2_avg1)
                min_average_position = number
            if A_2_avg2 < min(A_3_avg,A_2_avg1) and A_2_avg2< min_average:
                min_average = A_2_avg2
                min_average_position = number + 1
    return min_average_position

class testsolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(A = [4,2,2,5,1,5,8]), 1)

    def test_2(self):
        self.assertEqual(solution(A = [4,4]), 0)
        
if __name__ == '__main__':
    unittest.main()