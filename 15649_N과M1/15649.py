from sys import stdin
import itertools

n, m = map(int, stdin.readline().split())
arr = [i for i in range(1, n+1)]
nPr = itertools.permutations(arr, m)
for p in nPr:
    for j in p:
        print(j, end=" ")
    print()