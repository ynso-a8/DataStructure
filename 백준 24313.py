# -*- coding: utf-8 -*-
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if c > a1:
    ans = a0 <= n0 * (c - a1)
    print(1 if ans else 0)
elif c < a1:
    print(0)
else:
    print(0 if a0 > 0 else 1)