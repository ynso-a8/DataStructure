# -*- coding: utf-8 -*-
n = int(input())
ans = []        #�� �迭
series = []     #�Է°���
stack = []
flag = 1        #ans ������� NO ������� ������ ����
push_count = 0

series.append(int(input()))
for i in range(series[0]):
    stack.append(i + 1)
    ans.append('+')
    push_count += 1
stack.pop()
ans.append('-')

for i in range(1, n):
    series.append(int(input()))

    if series[i] > series[i - 1]:
        start = push_count
        for j in range(start, series[i]):
            stack.append(j + 1)
            ans.append('+')
            push_count += 1
        stack.pop()
        ans.append('-')
    else:
        if stack.pop() == series[i]:
            ans.append('-')
        else:
            flag = 0
            break

if flag:
    print(*ans, sep = '\n')
else:
    print('NO')