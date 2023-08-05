# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    ground = [[0 for j in range(m)] for i in range(n)]
    info = []
    for _ in range(k):
        y, x = map(int, stdin.readline().split())
        ground[x][y] = 1
        info.append([x,y])

    search, ans = deque([]), 0
    for coord in info:
        x, y = coord[0], coord[1]
        if ground[x][y] == 1:
            search.append([x,y])

            while len(search) != 0:
                temp = search.popleft()
                x, y = temp[0], temp[1]
                if ground[x][y] == 1:
                    ground[x][y] = 0

                    if x > 0 and ground[x - 1][y] == 1:    #╬у
                        search.append([x-1,y])
                    if x < n - 1 and ground[x + 1][y] == 1:    #╣з
                        search.append([x+1,y])

                    if y > 0 and ground[x][y - 1] == 1:    #аб
                        search.append([x,y-1])
                    if y < m - 1 and ground[x][y + 1] == 1:    #©Л
                        search.append([x,y+1])
            ans += 1

    print(ans)