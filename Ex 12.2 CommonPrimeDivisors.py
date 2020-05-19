# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:04:14 2020
Thanks for the help from my briliant girlfriend
first find the gcd of a and b
multiply the remainder and find the gcd of the remainder and the first gcd
update the remainder by dividing the remainder with the new gcd
continue until we arrive remainder == 1 or gcd_new == 1, in the first cases all the remainder 
are within the gcd, in the second case there are extra prime number
@author: frank
"""
import unittest
Z_range = range(1,int(6e3+1))

def solution(A,B):
    
    def gcd(N,M):
        if N % M ==0:
            return M
        else:
            return gcd(M,N % M)
    
    index  = 0
    count = 0
    for index in range(len(A)):
        a = A[index]
        b = B[index]
        gcd_1 = gcd(a,b)
        a_1 = a / gcd_1
        b_1 = b / gcd_1
        surplus = a_1 * b_1
        while True:    
            gcd_new = gcd(surplus,gcd_1)
            surplus = surplus / gcd_new
            if surplus == 1:
                count += 1
                break
            elif gcd_new == 1:
                break
    
        index += 1
    
    return count 

class testsolution(unittest.TestCase):
    def test_1(self):
        A = [15, 10, 3]
        B = [75, 30, 5]
        self.assertEqual(solution(A,B),1)

if __name__ == "__main__":
    unittest.main()