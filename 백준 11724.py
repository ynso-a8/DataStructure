# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def bfs(start, edge, visited):
    search = deque([start])

    while search:
        value = search.popleft()
        visited[value] = True

        for i in edge[value]:            
            if not visited[i]:
                visited[i] = True
                search.append(i)


n, m = map(int, stdin.readline().split())
visited = [False] * (n + 1)
edge = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)

ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        bfs(i, edge, visited)
        ans += 1
        
print(ans)