def amount_of_d(n, d):
    count = 0

    while n != 0:
        n //= d
        count += n

    return count

n, m = map(int, input().split())

if m > n - m:
    m = n - m

over2 = amount_of_d(n, 2) - amount_of_d(n - m, 2)
over5 = amount_of_d(n, 5) - amount_of_d(n - m, 5)

below2 = amount_of_d(m, 2)
below5 = amount_of_d(m, 5)

total2 = over2 - below2
total5 = over5 - below5

print(total5 if total5 < total2 else total2)
