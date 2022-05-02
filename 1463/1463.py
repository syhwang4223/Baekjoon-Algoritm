n = int(input())

dp = [0 for i in range(n+1)]
#dp[i]: 정수 i에, 주어진 연산 세 개를 사용해서 1을 만들 때 최소횟수

dp[1] = 0
for i in range(2,n+1):
    tmp = []
    if i%2==0:
        tmp.append(dp[i//2])
    if i%3==0:
        tmp.append(dp[i//3])
    tmp.append(dp[i-1])
    dp[i] = min(tmp)+1

print(dp[-1])    
