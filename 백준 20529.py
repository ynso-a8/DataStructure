# -*- coding: utf-8 -*-
from math import dist
from sys import stdin
from collections import deque

info = {'E': 0, 'I': 1,
        'S': 0, 'N': 1,
        'T': 0, 'F': 1,
        'P': 0, 'J': 1}

def exchange(mbti):
    result = []
    for c in mbti:
        result.append(info[c])

    return result

def distance(a, b):
    ans = 0
    for i in range(4):
        ans += (a[i] - b[i]) * (a[i] - b[i])
    return ans

t = int(stdin.readline().rstrip())

for _ in range(t):
    n = int(stdin.readline().rstrip())
    data = list(stdin.readline().split())
    for i in range(n):
        data[i] = exchange(data[i])

    if n > 32:
        print(0)
    else:    
        far = []
        for i in range(n - 2):
            far.append(32)
            for j in range(i + 1, n - 1):
                c1 = distance(data[i], data[j])
                for k in range(j + 1, n):
                    c2 = distance(data[i], data[k]) + distance(data[j], data[k])
                    if far[i] > c1 + c2:
                        far[i] = c1 + c2

        print(min(far))