# -*- coding: utf-8 -*-
import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a, b = map(int, input().split()) #a/b + c/d = over/below
c, d = map(int, input().split())

over = a*d + b*c
below = b*d

if over >= below:
    a, b = over, below
else:
    a, b = below, over
    
factor = gcd(a, b)
over //= factor
below //= factor

print(over, below)