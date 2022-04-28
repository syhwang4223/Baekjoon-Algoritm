from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
lis = [0]
for a in arr:
    if a > lis[-1]:
        lis.append(a)
    else:
        lis[bisect_left(lis, a)] = a

print(len(lis) - 1)