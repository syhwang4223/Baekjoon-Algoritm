from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
graph = []

day = 0
q = deque()

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j,0))           



while q:
    row, col, day = q.popleft()
    if graph[row][col] != 1: continue
    
    for nxtRow, nxtCol in [(row,col+1), (row,col-1), (row+1,col), (row-1,col)]:

        if nxtRow < 0 or nxtRow >= n or nxtCol < 0 or nxtCol >= m:
            continue

        if graph[nxtRow][nxtCol] == 0:
            q.append((nxtRow,nxtCol,day+1))
            graph[nxtRow][nxtCol] += 1

        
for g in graph:
    if 0 in g:
        print(-1)
        exit()
print(day)
