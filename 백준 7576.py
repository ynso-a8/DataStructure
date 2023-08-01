# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
data = [[0] * m for j in range(n)]
info = deque([])

for i in range(n):
    data[i] = list(map(int, stdin.readline().split()))
    for j in range(m):            
        if data[i][j] == 1:
            info.append([i, j])

day = -1
L = len(info)
while L != 0:
    day += 1
    for _ in range(L):
        pos = info.popleft()
        x, y = pos[0], pos[1]
         
        if x > 0 and data[x - 1][y] == 0:    #╬у
            data[x - 1][y] = 1
            info.append([x-1,y])
        if x < n - 1 and data[x + 1][y] == 0:    #╣з
            data[x + 1][y] = 1
            info.append([x+1,y])

        if y > 0 and data[x][y - 1] == 0:    #аб
            data[x][y - 1] = 1
            info.append([x,y-1])
        if y < m - 1 and data[x][y + 1] == 0:    #©Л
            data[x][y + 1] = 1
            info.append([x,y+1])
    L = len(info)

ans = 1
for i in data:
    for j in i:
        ans *= j
        if ans == 0:
            break
    if ans == 0:
            break

if ans == 0:
    print(-1)
else:
    print(day)