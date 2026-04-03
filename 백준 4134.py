from sys import stdin

def is_prime(n): #3 이상의 입력값
    if n % 2 == 0:
        return 0

    for r in range(3, int(n**0.5) + 1, 2):
        if n % r == 0:
            return 0
        
    return 1

t = int(stdin.readline().rstrip())
next = [1, 2, 1, 4, 3, 2, 1, 2, 1, 2] #1의 자리 경우 따져서 다음 후보 수 구하는 배열

for _ in range(t):
    n = int(stdin.readline().rstrip())

    if n <= 2:
        print(2)
    
    elif n == 4:
        print(5)

    else:
        while (is_prime(n) == 0):
            n += next[n%10]
        print(n)

