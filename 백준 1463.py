# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

n = int(input())
least = [0] * (n + 1)

for i in range(2, n + 1):
    a, b, c = n, n, n
    if i % 3 == 0:
        a = least[i // 3] + 1
    if i % 2 == 0:
        b = least[i // 2] + 1
    c = least[i - 1] + 1

    least[i] = min(a, b, c)

print(least[n])