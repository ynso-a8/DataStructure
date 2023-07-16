k, n = map(int, input().split())
inventory = []
big = 0

for _ in range(k):
    temp = int(input())
    inventory.append(temp)
    if temp > big:
        big = temp

start = 0
end = mid = big

while mid != start:    
    total = 0

    for i in inventory:
        total += i // mid

    if total < n:
        end = mid
    else:
        start = mid

    mid = (start + end) // 2

print(mid)