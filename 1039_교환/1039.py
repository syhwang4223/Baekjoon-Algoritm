from sys import stdin
from collections import deque

n, k = stdin.readline().split()
n = list(n)
m = len(n)
k = int(k)

chk = [[False for _ in range(11)] for _ in range(1000001)]
q = deque()
q.append((n, 0))
chk[int(''.join(n))][0] = True


def swap(n, i, j):
    tmp = n[i]
    n[i] = n[j]
    n[j] = tmp


answer = -1
while q:
    n, depth = q.popleft()

    if depth == k:
        answer = max(answer, int(''.join(n)))
        continue
    for i in range(m):
        for j in range(i + 1, m):
            if i == 0 and n[j] == '0':
                continue
            swap(n, i, j)
            n_int = int(''.join(n))
            if not chk[n_int][depth + 1]:
                chk[n_int][depth + 1] = True
                q.append((n.copy(), depth + 1))
            swap(n, i, j)

print(answer)