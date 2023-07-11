# -*- coding: utf-8 -*-

def compare(str1, str2):
    a = len(str1)
    b = len(str2)
    small = min(a, b)

    for i in range(0, small):
        result = ord(str1[i]) - ord(str2[i])
        if result:
            return result

    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1

def binarysearch(target, arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2;

        result = compare(target, arr[mid])
        if result == 0:
            return mid
        elif result < 0:
            end = mid - 1
        else:
            start = mid + 1

    return -1

n, m = map(int, input().split())
names = [[0 for j in range(2)] for i in range(n)]
index = []
for i in range(0, n):
    name = input()
    index.append(name)
    names[i][0] = name
    names[i][1] = i

names.sort(key = lambda x : x[0])
c = [i[0] for i in names]

for j in range(0, m):
    s = input()
    try:
        s = int(s)
        print(index[s - 1])
    except:        
        ans = names[binarysearch(s, c)][1]
        print(ans + 1)