isbn = list(input())
total, x = 0, 0 #total은 isbn 숫자 합, x는 값이 손실된 위치
for i in range(13):
    if isbn[i] == '*':
        x = i
        isbn[i] = 0
    else:
        isbn[i] = int(isbn[i])

for i in range(6):
    total += isbn[2*i] + 3*isbn[2*i + 1]

total = ((total + isbn[-1]) % 10) or 10

if x%2:
    if total % 3 == 0:
        total -= 3
    print(3-total//3 + 3*((total%3 or 3) - 1))
else:
    print(10 - total)
