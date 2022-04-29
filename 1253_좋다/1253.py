from sys import stdin
from itertools import combinations

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

ans = 0
for i in range(n):
    tmp = arr[:i] + arr[i + 1:] # 해당 수 제외한 나머지 배열
    # 투 포인터
    left, right = 0, len(tmp) - 1
    while left < right:
        s = tmp[left] + tmp[right]
        if s == arr[i]:
            ans += 1
            break
        elif s < arr[i]:
            left += 1
        else:
            right -= 1

print(ans)

