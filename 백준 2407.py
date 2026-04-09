from sys import stdin

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a%b
    return a

n, m = map(int, stdin.readline().split())
if m > n//2:
    m = n - m

over, below = 1, 1

for i in range(1, m+1):
    over *= n + 1 - i
    below *= i

    r = gcd(over, below)

    over //= r
    below //= r

print(over)