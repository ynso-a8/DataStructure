# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
data = [[[0] * m for j in range(n)] for i in range(h)]
info, t = deque([]), 0

for i in range(h):
    for j in range(n):
        data[i][j] = list(map(int, stdin.readline().split()))
        for k in data[i][j]:            
            if k == 1:
                info.append([i, j, t])
            t = (t + 1) % m

day = -1
L = len(info)
while L != 0:
    day += 1
    for _ in range(L):
        pos = info.popleft()
        z, y, x = pos[0], pos[1], pos[2]

        if z > 0 and data[z - 1][y][x] == 0:    #아래    
            data[z - 1][y][x] = 1
            info.append([z-1,y,x])
        if z < h - 1 and data[z + 1][y][x] == 0:    #위 
            data[z + 1][y][x] = 1
            info.append([z+1,y,x])
         
        if y > 0 and data[z][y - 1][x] == 0:    #앞
            data[z][y - 1][x] = 1
            info.append([z,y-1,x])
        if y < n - 1 and data[z][y + 1][x] == 0:    #뒤
            data[z][y + 1][x] = 1
            info.append([z,y+1,x])

        if x > 0 and data[z][y][x - 1] == 0:    #좌
            data[z][y][x - 1] = 1
            info.append([z,y,x-1])
        if x < m - 1 and data[z][y][x + 1] == 0:    #우
            data[z][y][x + 1] = 1
            info.append([z,y,x+1])
    L = len(info)

ans = 1
for i in data:
    for j in i:
        for k in j:
            ans *= k
            if ans == 0:
                break
        if ans == 0:
                break
    if ans == 0:
                break

if ans == 0:
    print(-1)
else:
    print(day)