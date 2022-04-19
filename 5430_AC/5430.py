from sys import stdin
from collections import deque


t = int(stdin.readline())

for _ in range(t):
    # 각 테스트 케이스 에 대한 입력
    p = stdin.readline().rstrip()
    n = int(input())
    arr = deque(stdin.readline().strip("[]\n").split(','))
    error = False

    if n == 0:
        arr = deque()

    reverse = False
    # 함수 수행
    for f in p:
        if f == 'R':
            reverse = not reverse
        else: # f == 'D'
            if not arr:
                print("error")
                error = True
                break
            elif reverse:
                arr.pop()
            else:
                arr.popleft()

    # 결과 출력
    if reverse:
        arr.reverse()
    if not error:
        print("[" + ",".join(arr) + "]")