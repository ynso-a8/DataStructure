# -*- coding: utf-8 -*-
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
data = []
for _ in range(n):
    data.append(list(map(int, stdin.readline().split())))

ans = [0, 0]

def decompose(arr, size, ans):
    if size == 1:
        ans[arr[0][0]] += 1
        return
        
    total = 0
    for i in arr:
        for j in i:
            total += j

    if total == 0 or total == size * size:
        ans[arr[0][0]] += 1
        return

    mid = size // 2
    a, b, c, d = [], [], [], []
    for i in range(mid):
        a.append(arr[i][:mid])
        b.append(arr[i][mid:])

    for i in range(mid, size):
        c.append(arr[i][:mid])
        d.append(arr[i][mid:])

    decompose(a, mid, ans)
    decompose(b, mid, ans)
    decompose(c, mid, ans)
    decompose(d, mid, ans)

decompose(data, n, ans)
print(ans[0])
print(ans[1])
