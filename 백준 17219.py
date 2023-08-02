# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def compare(a, b):
    A, B = len(a), len(b)
    short = A if A > B else B

    for i in range(short):
        result = ord(a[i]) - ord(b[i]) 
        if result < 0:
            return -1
        elif result > 0:
            return 1

    if A == B:
        return 0
    elif A > B:
        return 1
    else:
        return -1
    
def binarysearch(info, target):
    start, end = 0, len(info) - 1

    while start <= end:
        mid = (start + end) // 2
        result = compare(info[mid][0], target)

        if result == 0:
            return mid
        elif result < 0:
            start = mid + 1
        else:
            end = mid - 1


n, m = map(int, stdin.readline().split())
info = []

for _ in range(n):    
    info.append(stdin.readline().split())

info.sort(key = lambda x: x[0])

for _ in range(m):
    temp = stdin.readline().rstrip()
    print(info[binarysearch(info, temp)][1])
