# -*- coding: utf-8 -*-
from sys import stdin

n = int(input())
queue = []
front = 0
rear = 0

for _ in range(n):
    cmd = stdin.readline().split()
    
    if cmd[0] == 'pop':
        if front != rear:
            print(queue[front])
            front += 1
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(rear - front)
    elif cmd[0] == 'empty':
        print(1 if front == rear else 0)
    elif cmd[0] == 'front':
        print(queue[front] if front != rear else -1)
    elif cmd[0] == 'back':
        print(queue[rear-1] if front != rear else -1)
    else:
        queue.append(int(cmd[1]))
        rear += 1