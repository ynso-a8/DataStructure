# -*- coding: utf-8 -*-
def gcd(a, b):
    if b == 0:
        return a
    a = a % b

    return gcd(b, a)

a, b = map(int, input().split())
ans = 0
if a < b:
    ans = gcd(b, a)
else:
    ans = gcd(a, b)

a /= ans
b /= ans
print(int(ans * a * b))
