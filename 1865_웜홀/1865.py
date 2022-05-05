from sys import stdin
INF = int(1e9)


def testcase():
    # 지점의 수, 도로의 수, 웜홀의 수
    n, m, w = map(int, stdin.readline().split())
    graphs = []

    # 도로 정보 입력
    for _ in range(m):
        s, e, t = map(int, stdin.readline().split())
        graphs.append((s, e, t))
        graphs.append((e, s, t))
    # 웜홀 정보 입력
    for _ in range(w):
        s, e, t = map(int, stdin.readline().split())
        graphs.append((s, e, -t))

    # 벨만 포드 알고리즘
    # 1. 출발 노드를 설정한다.
    # 2. 최단 거리 테이블을 초기화한다.
    # 3. 다음의 과정을 v-1 번 반복한다.
    #   1) 모든 간선 e 개를 하나 씩 확인한다.
    #   2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
    # 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번 과정을 한번 더 수행한다.
    # -> 이 떄 최단거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것이다.

    # 음의 사이클이 존재하면 True, 존재하지 않으면 False를 반환한다.
    def bellman_ford(start):
        # 최단거리 테이블
        distance = [INF for i in range(n + 1)]
        distance[start] = 0
        # 음의 사이클 판별을 위해 n(v) 번 반복
        for i in range(n):
            # 반복마다 모든 간선 확인
            for cur, nxt, dist in graphs:
                cost = distance[cur] + dist
                # 현재 노드를 거쳐 다음 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[nxt]:
                    distance[nxt] = cost
                    # n번 째에도 갱신이 발생하면 음의 사이클이 존재하는 것
                    if i == n-1:
                        return True
        return False

    # 어디서 출발하든 음의 사이클이 존재하면 시간단축이 가능한 것
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")




tc = int(stdin.readline())
for _ in range(tc):
    testcase()
