#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    chaotic = ''
    num_swaps = 0
    for i in range(len(q)):
        if(q[i]>i+3):
            chaotic += 'Too chaotic'
        for j in range(max(0,q[i]-2),i):
            if(q[i]<q[j]):
                num_swaps+=1

    if('Too chaotic' in chaotic):
        print('Too chaotic')
    else:
        print(num_swaps)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
