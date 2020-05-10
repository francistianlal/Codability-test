# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:49:21 2020

This is a challenging question but not hard
Build a reference for every letter first betfore looping through P and G
This greatly reduce complexity

Also remember to condsider the letter on the boundry and P,Q = 2,4 and the letter on position 2 need to
be taken extra attention
@author: frank
"""
import unittest

def solution(S,P,Q):
    
# first make a reference for every gene so we don't need to loop through the string again and again
    ref = {'A':1,'C':2,'G':3,'T':4}
    ref_count = {'A':0,'C':0,'G':0,'T':0}
    A = []
    C = []
    G = []
    T = []
    for letter in S:
        ref_count[letter] += 1
        A.append(ref_count['A'])
        C.append(ref_count['C'])
        G.append(ref_count['G'])
        T.append(ref_count['T'])
# now loop through the given array
    Min_value = []
    for index in range(0,len(P)):
        if Q[index] == P[index]:
            Min_value.append(ref[S[Q[index]]])
        if A[Q[index]] - A[P[index]] > 0:
            Min_value.append(min(ref['A'],ref[S[P[index]]]))
            continue
        if C[Q[index]] - C[P[index]] > 0:
            Min_value.append(min(ref['C'],ref[S[P[index]]]))
            continue
        if G[Q[index]] - G[P[index]] > 0:
            Min_value.append(min(ref['G'],ref[S[P[index]]]))
            continue
        if T[Q[index]] - T[P[index]] > 0:
            Min_value.append(min(ref['T'],ref[S[P[index]]]))
            continue
    return Min_value

class solutiontest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('CAGCCTA',[2,5,0],[4,5,6]),[2,4,1])


if __name__ =='__main__':
    unittest.main()