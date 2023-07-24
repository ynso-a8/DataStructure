# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

t = int(input())

for _ in range(t):
    command = stdin.readline().rstrip()
    r, front, rear = 0, 0, 0
    for ch in command:
        if ch == 'D':
            if r % 2 == 0:
                front += 1
            else:
                rear += 1
        else: #ch == 'R'
            r += 1

    n = int(stdin.readline())
    arr = stdin.readline().rstrip()
    
    if n >= front + rear:
        ans = []
        arr = arr[1:-1].split(',')
        for i in range(front, n - rear):
            ans.append(int(arr[i]))
        if r % 2 != 0:
            ans.reverse()

        print('[', end = '')
        print(*ans, sep = ',', end = '')
        print(']')
    else:
        print('error')