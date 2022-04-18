from sys import stdin


n = int(stdin.readline())
m = int(stdin.readline())
maps = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    # 시작 도시와 도착 도시를 연결 하는 노선은 하나가 아닐 수도 있다.
    if c < maps[a][b]:
        maps[a][b] = c

# 자기 자신 으로 연결 되는 간선 비용 초기화
for i in range(1, n+1):
    maps[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            maps[a][b] = min(maps[a][k] + maps[k][b], maps[a][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if maps[i][j] < int(1e9):
            print(maps[i][j], end=" ")
        else:
            print(0, end=" ")
    print("")
