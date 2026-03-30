from sys import stdin

n = int(stdin.readline().rstrip())
data = [] #입력값
high = 0 #최댓값

for _ in range(n):
    data.append(int(stdin.readline().rstrip()))
high = max(data)

integers = [1 for _ in range(high + 1)]
for i in range(2, high + 1, 2):
    integers[i] = 0
integers[2] = 1

for i in range(3, high//3 + 1, 2):
    if integers[i]:
        j = i * 3
        while (j <= high):
            integers[j] = 0
            j += i * 2

primes = [2]
for i in range(3, high + 1, 2):
    if integers[i]:
        primes.append(i)

for i in data:
    ans = 0 #해당 i 값의 골드바흐 파티션 개수
    for j in primes:
        temp = i - j
        half = i / 2
        if temp >= half and integers[temp]:
            ans += 1
    print(ans)
