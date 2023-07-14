t = int(input())

for i in range(0, t):
    n = int(input())
    kinds = []
    amounts = []

    for j in range(0, n):
        name, kind = input().split()

        if kind in kinds:
            pos = kinds.index(kind)
            amounts[pos] += 1
        else:
            kinds.append(kind)
            amounts.append(1)

    ans = 1
    for j in amounts:
        ans *= j + 1
    print(ans - 1)
