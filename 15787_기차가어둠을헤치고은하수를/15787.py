from sys import stdin

n, m = map(int, stdin.readline().split())
train = [0 for _ in range(n)]


for a in range(1, m + 1):
    tmp = list(map(int, stdin.readline().split()))
    command = tmp[0]
    i = tmp[1] - 1
    if len(tmp) == 3:
        x = tmp[2] -1

    if command == 1:
        # x번 째 좌석에 승객을 태운다
        train[i] |= (1 << x)
    elif command == 2:
        # x번 째 좌석의 승객을 하차 시킨다
        train[i] &= ~(1 << x)
    elif command == 3:
        train[i] = (train[i] << 1)
        # 좌석은 총 20 개
        if train[i] >= (1 << 20):
            train[i] %= (1 << 20)
    else:
        train[i] = (train[i] >> 1)


print(len(set(train)))
