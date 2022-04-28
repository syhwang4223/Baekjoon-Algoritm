from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graphs = [[] for _ in range(n + 1)]
l, r = 1, 1

for i in range(1, m + 1):
    a, b, c = map(int, stdin.readline().split())
    graphs[a].append((b, c))
    graphs[b].append((a, c))
    # 이진탐색 시 최대 범위 설정
    if c > r:
        r = c

start, end = map(int, stdin.readline().split())

ans = 0

while l <= r:
    # 운반 가능한 최대 중량
    mid = (l + r) // 2

    # bfs
    chk = [False for _ in range(n + 1)]
    chk[start] = True
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        for nxt, w in graphs[cur]:
            if not chk[nxt] and mid <= w:
                chk[nxt] = True
                q.append(nxt)

    if chk[end]:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)