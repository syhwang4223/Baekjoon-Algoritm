n = int(input())
dp = [-1 for i in range(n+1)]

if n==3:
    print(1)
    exit()
if n==4:
    print(-1)
    exit()

dp[3] = 1
dp[5] = 1

for i in range(6,n+1):
    tmp = []
    if dp[i-3]>0: tmp.append(dp[i-3])
    if dp[i-5]>0: tmp.append(dp[i-5])
    if tmp:
        dp[i] = min(tmp)+1

print(dp[n])
