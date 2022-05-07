from sys import stdin
import heapq

# 정점의 개수 입력
v = int(stdin.readline())
tree = [[] for _ in range(v+1)]

# 트리 정보 입력
for _ in range(v):
    tmp = list(map(int, stdin.readline().split()))
    a = tmp[0]
    for i in range(1, len(tmp)-1, 2):
        tree[a].append((tmp[i], tmp[i+1]))

# 모든 간선은 양방향인지? 음의 간선이 존재하는지? 에 대한 문제 조건 없음
# dfs 로 분류되어 있지만 다익스트라로도 풀 수 있음


def dijkstra(start):
    distance = [int(1e9) for _ in range(v + 1)]
    distance[start] = 0
    hq = [(start, 0)]

    while hq:
        cur, dist = heapq.heappop(hq)
        if dist < distance[cur]:
            continue
        for k in tree[cur]:
            cost = distance[cur] + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(hq, (k[0], cost))

    return distance


# 트리의 지름의 양 끝 점을 a, b라 하자.
# 이 떄 트리의 어느 정점에서든, 그 정점과 가장 먼 곳에 있는 정점은 a 또는 b이다.
# 따라서 다익스트라 함수 v번이 아닌 2번만에 정답을 알아낼 수 있다.

d1 = dijkstra(1)[1:]
a = d1.index(max(d1)) + 1
d2 = dijkstra(a)[1:]
print(max(set(d2) - {int(1e9)}))

