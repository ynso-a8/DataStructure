from sys import stdin

n = int(stdin.readline().rstrip())
ballons = list(map(int, stdin.readline().split()))
current_index = 0

for _ in range(n - 1):
    print(current_index + 1, end = ' ')
    distance = ballons[current_index]
    direction = 1 if distance > 0 else -1
    distance *= direction
    ballons[current_index] = 0

    while distance > 0:
        current_index = (current_index + direction) % n
        if ballons[current_index] != 0:
            distance -= 1

print(current_index + 1)