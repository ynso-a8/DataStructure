from sys import stdin

n = int(input())
ans = 0
arr = [int(stdin.readline().rstrip())]
for i in range(n-1):
    arr.append(int(stdin.readline().rstrip()))
    if arr[-2] > arr[-1]:
        ans += 1

print(ans + 1)