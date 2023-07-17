# -*- coding: utf-8 -*-
n = int(input())
ans = []        #답 배열
series = []     #입력값들
stack = []
flag = 1        #ans 출력할지 NO 출력할지 결정할 변수
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