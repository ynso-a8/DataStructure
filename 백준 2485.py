from sys import stdin

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a%b
    
    return a

n = int(stdin.readline().rstrip())
pos = [int(stdin.readline().rstrip())]
offset = []

for _ in range(n-1):
    temp = int(stdin.readline().rstrip())
    offset.append(temp - pos[-1])
    pos.append(temp)

gap = min(offset)
factor = gcd(offset[0], gap)

for i in offset:
    temp = gcd(i, gap)

    if temp < factor:
        factor = temp
    if temp == 1:
        break

print((pos[-1] - pos[0])//factor + 1 - n)


