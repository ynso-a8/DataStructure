# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
mapdata = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    row = stdin.readline().rstrip()
    mapdata.append([int(c) for c in row])   

total = 0
info = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start):
    search = deque([])
    search.append(start)
    x, y = start
    visited[x][y] = True
    count = 0

    while search:
        x, y = search.popleft()         
        visited[x][y] = True
        count += 1

        for k in range(4):
            i, j = x + dx[k], y + dy[k]

            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or not mapdata[i][j]:
                continue

            visited[i][j] = True
            search.append([i, j])

    return count

for i in range(0, n):
    for j in range(0, n):
        if mapdata[i][j] and not visited[i][j]:            
            total += 1
            info.append(bfs([i, j]))

info.sort()

print(total)
for t in info:
    print(t)