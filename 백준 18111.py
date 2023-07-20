# -*- coding: utf-8 -*-
n, m, b = map(int, input().split())
info = [[0]*m for _ in range(n)]

for i in range(n):
    info[i] = list(map(int, input().split()))

time = 2147483647
height = 0

for h in range(257):
    addcount = 0
    minuscount = 0
    for i in range(n):
        for j in range(m):
            if info[i][j] < h:
                addcount += h - info[i][j]
            else:
                minuscount += info[i][j] - h
    
    if addcount > minuscount + b:
        continue

    ans = addcount + minuscount * 2

    if ans < time:
        time = ans
        height = h

print(time, height)