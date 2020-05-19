# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:57:24 2020

@author: frank
"""
import unittest
NM_range = range(1,int(3e4+1))

def ok(A,B,C,mid):
    # count values in C
    cnt=[0]*(2*len(C)+1)
    for i in C[:mid+1]: 
        cnt[i]+=1
    # prefix sum: accumulate sum of cnt
    for i in range(1,len(cnt)): 
        cnt[i]+=cnt[i-1]
    # if sum between A[i]~B[i] is 0, then plank i can not be covered
    for a,b in zip(A,B):
        if cnt[b]==cnt[a-1]: 
            return False
    return True
    
    
def solution(A, B, C):
    # binary search
    result = 40000
    low , high = 0, len(C)-1
    while low <= high:
        mid=(low + high)//2
        if ok(A,B,C,mid):
            result=min(result, mid + 1)
            high = mid - 1
        else:
            low = mid + 1
    if result == 40000:
        return -1
    return result

class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,4,5,8]
        B = [4,5,9,10]
        C = [4,6,7,10,2]
    
        self.assertEqual(solution(A,B,C),4)
  
if __name__ == "__main__":
    unittest.main()



