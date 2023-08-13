from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
maze = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    row = stdin.readline().split()
    maze.append([int(c) for c in row])
    for j in range(m):
        if maze[i][j] == 2:
            start = [i, j]
            maze[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

search = deque([start])
visited[start[0]][start[1]] = True

while search:
    x, y = search.popleft()
    visited[x][y] = True

    for k in range(4):
        i, j = x + dx[k], y + dy[k]

        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or not maze[i][j]:
            continue

        maze[i][j] += maze[x][y]
        search.append([i, j])
        visited[i][j] = True

for i in range(n):
    for j in range(m):
        print(maze[i][j] if visited[i][j] or not maze[i][j] else -1, end = ' ')
    print()
