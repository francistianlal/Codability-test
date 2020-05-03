# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:44:17 2020
Ex 1.1
Binary Gap problem
1. Give a positive integer number
2. Return the length of its longest binary gap

very simple question but I miss the extreme cases at the first try
the gap mean there have to be two switches happened before the count in between make sense

@author: frank tian
"""
# define the range
N_range = range(1, 2147483647 + 1)
N = 51712
def solution(N):
    # convert the number
    if N not in N_range:
        raise TypeError('N is not in range')
    N_bin = bin(N)[2:]
    # define the last number which help define switching point
    last_number = None
    count = 0
    count_max = 0
    switch = 0
    Trigger = False
    for number in list(N_bin):
        if last_number != None and number != last_number:
            switch += 1
            if switch == 2 and count > count_max:
                count_max = count
            if switch == 2:
                switch =1
            count = 1
            Trigger = True
            

        if Trigger and number == last_number:
            count += 1

        last_number = number
    return count_max
    
        
    