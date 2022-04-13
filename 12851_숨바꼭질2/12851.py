from collections import deque

n, k = map(int, input().split())
chk = [False for i in range(200001)]

q = deque([(n, 0)])
chk[n] = True
cnt = 0
mini = 0
first = True

while q:
    cur, time = q.popleft()
    chk[cur] = True
    # print(cur, time, trace)
    # 처음 도착했을 땐 그게 최소시간이지만
    if cur == k and first:
        print(time)
        cnt += 1
        mini = time
        first = False
    # 그 다음에 도착했을 땐 최소 시간인 경우에만 답으로 인정
    elif cur == k and time == mini:
        cnt += 1

    for nxt in [cur - 1, cur + 1, 2 * cur]:
        if 0 <= nxt <= 100000 and not chk[nxt]:
            # chk[nxt] = True
            q.append((nxt, time+1))
print(cnt)


