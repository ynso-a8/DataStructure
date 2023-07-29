# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

t = int(input())

ways = [0] * 11
ways[1] = 1
ways[2] = 2
ways[3] = 4

for i in range(4, 11):
    ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

for _ in range(t):
    n = int(stdin.readline().rstrip())
    print(ways[n])   