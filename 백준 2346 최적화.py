from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
balloons = deque(enumerate(map(int, stdin.readline().split()), start=1))
result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(idx)
    
    if not balloons:
        break
    
    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(*(result))