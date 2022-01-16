from sys import stdin
import heapq
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, stdin.readline().split())
    graph[a].append((c,b))

s,e = map(int, stdin.readline().split())
q = [(0,s)]
dist = [INF for _ in range(n+1)]
dist[s] = 0

while q:
    cost, cur = heapq.heappop(q)

    if dist[cur] < cost:
        continue

    for c, nxt in graph[cur]:
        if dist[nxt] > dist[cur] + c:
            dist[nxt] = dist[cur] + c
            heapq.heappush(q, (dist[nxt],nxt))

print(dist[e])
