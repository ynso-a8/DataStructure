# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

m = int(stdin.readline().rstrip())

myset = [0] * 20

for _ in range(m):
    cmd = stdin.readline().split()
    if len(cmd) == 2:
        i = int(cmd[1]) - 1

    if cmd[0] == 'add':
        myset[i] = 1
    elif cmd[0] == 'check':
        print(myset[i])
    elif cmd[0] == 'remove':
        myset[i] = 0
    elif cmd[0] == 'toggle':
        myset[i] = 1 if myset[i] == 0 else 0
    elif cmd[0] == 'all':
        for j in range(20):
            myset[j] = 1
    else:
        for j in range(20):
            myset[j] = 0
