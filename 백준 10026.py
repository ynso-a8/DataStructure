# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

n = int(input())
data = []
visited = [[False] * n for _ in range(n)]
for _ in range(n):
    temp = stdin.readline().rstrip()
    data.append([s for s in temp])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def separated(start, color):

    info = deque([start])
    visited[start[0]][start[1]] = True
    while info:
        x, y = info.popleft()        

        for k in range(4):
            i = x + dx[k]
            j = y + dy[k]

            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j]:
                continue

            if data[i][j] == color:
                info.append([i, j])
                visited[i][j] = True       

def merged(start):

    info = deque([start])
    visited[start[0]][start[1]] = True
    while info:
        x, y = info.popleft()        

        for k in range(4):
            i = x + dx[k]
            j = y + dy[k]

            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j]:
                continue

            if data[x][y] == 'B' and data[i][j] == 'B':
                info.append([i, j])
                visited[i][j] = True
            elif data[x][y] != 'B' and data[i][j] != 'B':
                info.append([i, j])
                visited[i][j] = True


ans1, ans2 = 0, 0   #정상인, 색약인

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            separated([i, j], data[i][j])
            ans1 += 1

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            merged([i, j])
            ans2 += 1
            
print(ans1, ans2)

