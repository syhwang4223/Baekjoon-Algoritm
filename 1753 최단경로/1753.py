from sys import stdin
import heapq
INF = int(1e9)

v, e = map(int, stdin.readline().split())
s = int(stdin.readline())
graph = [[] for _ in range(v+1)]

#간선 정보 입력
for i in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c,b))

dist = [INF for _ in range(v+1)]

h = []
heapq.heappush(h, (0,s))
dist[s] = 0

while h:
    d, cur = heapq.heappop(h)

    #이미 방문한 노드는 무시
    if dist[cur] < d:
        continue

    for weight, nxt in graph[cur]:
        cost = dist[cur] + weight #현재 노드를 거쳐서 갈 때의 경로
        #경우하는게 더 빠르면 경로 업데이트
        if cost < dist[nxt]:
            dist[nxt] = cost
            heapq.heappush(h,(dist[nxt], nxt))

#정답 출력
for i in range(1,v+1):
    print(dist[i] if dist[i]<INF else "INF")


