from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
time = [-1 for i in range(100001)]

q = deque()
q.append(n)
time[n] = 0

while q:
    cur = q.popleft()
    if cur == k: break
    nxts = [cur-1, cur+1, 2*cur]
    for nxt in nxts:
        if nxt<0 or nxt>100000 or time[nxt]!=-1:
            continue
        q.append(nxt)
        time[nxt] = time[cur] + 1
        

print(time[k])
