from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())

answer=0

#k의 범위
row=1
high=k 

#k번째 수라는 것: B에 B[k]보다 작은 수가 k-1개 있다.

while row<=high:

    mid = (row+high)//2
    cnt = 0 # N*N행렬의 각 행에서 mid보다 작은 수들의 개수
    for i in range(1,n+1):
        cnt+= min(mid//i,n)

    if cnt>=k:
        answer=mid
        high=mid-1
    else:
        row=mid+1

print(answer)
