# -*- coding: utf-8 -*-
from sys import stdin

n = int(input())
m = int(input())
string = stdin.readline().rstrip()
i, info = 0, []

while i < m - 1:    #���ڿ� ��ȸ�ϸ鼭 P_n���� ��� ã�Ƽ� n���� info�� ����
    if string[i] == 'I':
        front, rear = i, i + 1
        while rear < m and string[front] != string[rear]:
            front = rear
            rear += 1

        if i != front and string[front] == 'I':
            info.append((front - i + 1) // 2)
            i = rear
        elif i != front and string[front] == 'O':
            info.append((front - i) // 2)
            i = rear + 1
        else:
            i += 1
    else:
        i += 1

ans = 0
for gap in info:
    if gap >= n:
        ans += gap - n + 1

print(ans)
            
