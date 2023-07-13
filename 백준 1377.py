n = int(input())
arr = []
for i in range(n):
    arr.append( [int(input()), i] )

sorted_arr = sorted(arr) 
answer = 0

for i in range(n):
    temp = sorted_arr[i][1] - arr[i][1]
    if answer < temp:
        answer = temp

print(answer + 1)