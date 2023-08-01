# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

def bfs(visited, edges, count = 0):
    search = deque([1])
    visited[1] = True

    while search:
        cur = search.popleft()

        for i in edges[cur]:
            if not visited[i]:
                visited[i] = True
                search.append(i)
                count += 1

    return count


n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
visited = [False for _ in range(n + 1)]
edges = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

print(bfs(visited, edges))
