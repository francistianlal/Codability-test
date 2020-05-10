# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:12:03 2020

@author: frank
"""
import unittest

N_range = range(0,int(1e5+1))
Element_range = range(0,int(2147483647+1))
intersection_max = int(1e7)


def solution(A):
    start, end = [], []
    for number, radius in enumerate(A):
        start.append(number - radius)
        end.append(number + radius)
    start.sort()
    end.sort()

    istart = 0
    intersections = 0
    for iend in range(len(end)):                                          # for every closing
        while istart < len(start) and start[istart] <= end[iend]:        # step through unreconciled openings
            istart += 1
        intersections += istart - iend - 1                                  # and record them as intersections

        if intersections > intersection_max:
            return -1

    return intersections
     
        
class solution_test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(A = [1,5,2,1,4,0]),11)

    def test_2(self):
        self.assertEqual(solution([1,1,1]),3)
        
if __name__ == '__main__':
    unittest.main()

