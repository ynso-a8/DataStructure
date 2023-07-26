# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def strcompare(A, B):
    a, b = len(A), len(B)
    small = min(a, b)

    for i in range(small):
        result = ord(A[i]) - ord(B[i])
        if result > 0:
            return 1
        elif result < 0:
            return -1

    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1
    

n, m = map(int, stdin.readline().split())
nohear, nosee = [], []
for _ in range(n):
    nohear.append(stdin.readline().rstrip())
for _ in range(m):
    nosee.append(stdin.readline().rstrip())

nohear = sorted(nohear)
nosee = sorted(nosee)

i, j, who = 0, 0, []
while i < n and j < m:
    result = strcompare(nohear[i], nosee[j])
    if result == 0:
        who.append(nohear[i])
        i += 1
        j += 1
    elif result == -1:
        i += 1
    else:
        j += 1

if i == n and j != m:
    while j < m:
        result = strcompare(nohear[-1], nosee[j])
        if result == 0:
            who.append(nohear[-1])
            break
        elif result == -1:
            break
        else:
            j += 1

if i != n and j == m:
    while i < n:
        result = strcompare(nohear[i], nosee[-1])
        if result == 0:
            who.append(nosee[-1])
            break
        elif result > 0:
            break
        else:
            i += 1

print(len(who))
for name in who:
    print(name)