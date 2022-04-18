from sys import stdin
from collections import deque

n = int(stdin.readline())

friends = [[0, ] for _ in range(n+1)]
while True:
    a, b = map(int, stdin.readline().split())
    if a == -1 and b == -1: break
    friends[a].append(b)
    friends[b].append(a)

# for f in friends:
#     print(f)
ans = []
candidate = []
leader = 51

# BFS
for i in range(1, len(friends)):
    chk = [False for _ in range(n+1)]
    q = deque([(i, 0)])
    chk[i] = True
    maxPoint = 1
    while q:
        cur, point = q.popleft()
        if point > maxPoint:
            maxPoint = point

        for j in friends[cur]:
            if j == 0:
                continue
            if not chk[j]:
                chk[j] = True
                q.append((j, point + 1))

    ans.append((i, maxPoint))


for member, point in ans:
    if point < leader:
        leader = point
for member, point in ans:
    if point is leader:
        candidate.append(member)

print(leader, len(candidate))
for c in candidate:
    print(c, end=" ")
