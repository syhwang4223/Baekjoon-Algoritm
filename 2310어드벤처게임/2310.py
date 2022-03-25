from sys import stdin
from collections import deque


def exploreMaze(n):
    maze = [('0', 0, [])]  # 방의 내용물, 금액, 다음방 번호들
    chk = [False for i in range(n + 1)]
    q = deque()
    pocket = 0  # 소지금

    for i in range(n):
        tmp = list(stdin.readline().split())
        roomType = str(tmp[0])
        money = int(tmp[1])
        nextRooms = list(map(int, tmp[2:-1]))
        maze.append((roomType, money, nextRooms))

    if maze[1][0] == 'T' and pocket < maze[1][2]:
        return "No"
    q.append(1)
    chk[1] = True

    while q:
        cur = q.popleft()
        if cur == n:
            return "Yes"

        roomType, money, nextRooms = maze[cur]
        if roomType == 'T':
            pocket -= money
        elif roomType == 'L':
            pocket = max(pocket, money)

        for nxt in nextRooms:
            if not chk[nxt] and not (maze[nxt][0] == 'T' and pocket < maze[nxt][1]):
                chk[nxt] = True
                q.append(nxt)

    return "No"


n = int(stdin.readline())

while n > 0:
    print(exploreMaze(n))
    n = int(stdin.readline())
