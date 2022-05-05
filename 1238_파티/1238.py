from sys import stdin
import heapq
INF = int(1e9)

n, m, x = map(int, stdin.readline().split())
graphs = [[] for _ in range(n+1)]
for _ in range(m):
    # 도로의 시작점, 끝점, 소요 시간
    start, end, t = map(int, stdin.readline().split())
    graphs[start].append((end, t))

result = [] # 각 학생 별 소요시간

# 다익스트라 알고리즘
# 1. 출발 노드를 설정한다
# 2. 최단 거리 테이블을 초기화한다
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3번과 4번을 반복한다.

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for nxt in graphs[now]:
            cost = dist + nxt[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0],))


# 모든 학생에 대해 다익스트라 알고리즘 수행
for i in range(1, n+1):
    # 갈 때
    distance = [INF for _ in range(n + 1)]
    dijkstra(i)
    go = distance[x]

    # 올 때
    distance = [INF for _ in range(n + 1)]
    dijkstra(x)
    back = distance[i]

    # 결과 리스트에 저장
    result.append(go + back)

print(max(result))



