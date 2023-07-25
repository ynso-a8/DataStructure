# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def ztravel(n, i, j, start, end):
    quad, half = 0, 2**(n-1)
    if i < half and j < half:
        quad = 0
    elif i < half and j >= half:
        quad = 1
        j -= half
    elif i >= half and j < half:
        quad = 2
        i -= half
    else:
        quad = 3
        i -= half
        j -= half

    start += quad * 2 ** (2*n - 2)
    end -= (3 - quad) * 2 ** (2*n - 2)

    if start == end:
        return start
    else:
        return ztravel(n-1, i, j, start, end)
    

n, r, c = map(int, stdin.readline().split())
start, end = 0, 2**(2*n) - 1
print(ztravel(n, r, c, start, end))