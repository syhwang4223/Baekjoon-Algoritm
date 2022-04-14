from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())

chicken = []
home = []

for i in range(n):
    tmp = list(map(int, stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 1:
            home.append((i+1, j+1))
        elif tmp[j] == 2:
            chicken.append((i+1, j+1))


mini = 100000

# 가능한 모든 치킨집 조합
for combi in combinations(chicken, m):
    totalDist = 0
    for h in home:
        # 각 집마다 가장 가까운 치킨집 과의 거리 구하기
        minDist = 100000
        for c in list(combi):
            dist = abs(h[0]-c[0]) + abs(h[1]-c[1])
            if dist < minDist:
                minDist = dist
        totalDist += minDist

    if totalDist < mini:
        mini = totalDist

print(mini)
