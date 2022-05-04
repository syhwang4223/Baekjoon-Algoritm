from sys import stdin
from collections import deque


# 위상 정렬, dp
def testcase():
    # 건물 수와 규칙 수 입력
    n, k = map(int, stdin.readline().split())

    # 건물을 짓는데 걸리는 시간 입력
    delays = [0] + list(map(int, stdin.readline().split()))
    orders = [[] for _ in range(n+1)]

    # 건물 짓기 순서 입력: x를 지은 뒤 y를 지을 수 있다.
    indegree = [0 for _ in range(n+1)] # 진입 차수
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        orders[x].append(y)
        indegree[y] += 1

    # 건설해야 할 건물의 번호
    w = int(stdin.readline())

    # 건물 i를 건설 완료 하는데 드는 최소 시간
    dp = [0 for _ in range(n + 1)]

    # 진입 차수가 0인 노드를 큐에 담는다
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delays[i]



    # 큐가 빌 때까지 반복
    while q:
        cur = q.popleft()
        for nxt in orders[cur]:
            # 진입 차수 하나 줄이고 dp값 갱신
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[cur] + delays[nxt])
            # 새롭게 진입 차수가 0이 되는 노드를 큐에 넣는다
            if indegree[nxt] == 0:
                q.append(nxt)

    print(dp[w])


t = int(stdin.readline())
for i in range(t):
    testcase()
