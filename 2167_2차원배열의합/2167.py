from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [[0 for _ in range(m+1)]]
for _ in range(n):
    arr.append([0] + list(map(int, stdin.readline().split())))


#(0,0) 부터 (r,c) 까지의 부분합
subsum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for r in range(1,n+1):
    for c in range(1,m+1):
        subsum[r][c] = subsum[r-1][c] + subsum[r][c-1] + arr[r][c] - subsum[r-1][c-1]
        

k = int(stdin.readline())
for _ in range(k):
    i,j,x,y = map(int, stdin.readline().split())
    print(subsum[x][y] - subsum[i-1][y] - subsum[x][j-1] + subsum[i-1][j-1])
