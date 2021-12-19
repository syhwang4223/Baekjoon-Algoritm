from sys import stdin

ropes = []
n = int(stdin.readline())

for i in range(n):
    r = int(stdin.readline())
    ropes.append(r)

ropes.sort()
ans = ropes[0]*n

for i in range(n):
    tmp = ropes[i]*(n-i)
    if tmp>ans:
        ans=tmp

print(ans)
