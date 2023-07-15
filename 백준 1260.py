def DFS(start, adjmatrix, size, check):
    print(start + 1, end = ' ')
    check[start] = 1

    for i in range(size):
        if adjmatrix[start][i] and check[i] == 0:
            adjmatrix[start][i] = adjmatrix[i][start] = 0
            DFS(i, adjmatrix, size, check)

def BFS(start, adjmatrix, check):
    size = len(adjmatrix)
    queue = []
    queue.append(start)

    while len(queue) != 0:
        cur = queue.pop(0)
        print(cur + 1, end = ' ')
        check[cur] = 1

        for i in range(size):
            if adjmatrix[cur][i]:
                adjmatrix[cur][i] = adjmatrix[i][cur] = 0
                if check[i] == 0:
                    check[i] = 1
                    queue.append(i)
                


n, m, v = map(int, input().split())
v -= 1

check1 = [0 for _ in range(n)]
check2 = [0 for _ in range(n)]
adjmatrix1 = [[0 for _ in range(n)] for _ in range(n)]
adjmatrix2 = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adjmatrix1[x][y] = adjmatrix1[y][x] = 1
    adjmatrix2[x][y] = adjmatrix2[y][x] = 1 

DFS(v, adjmatrix1, n, check1)
print()
BFS(v, adjmatrix2, check2)
