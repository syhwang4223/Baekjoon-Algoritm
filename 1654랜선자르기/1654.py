from sys import stdin

def binary(start,end,arr,target):
    global answer
    
    if start>end:
        return
    mid = (start+end)//2
    cnt = 0
    for l in lines:
        cnt+=l//mid


    if cnt>=target:#더 크게 잘라야 함
        answer=mid
        binary(mid+1,end,arr,target)
    else:#더 작게 잘라야 함
        binary(start,mid-1,arr,target)
        

global answer
answer = 0

k,n = map(int, stdin.readline().split())
lines = sorted(map(int,[stdin.readline().strip() for i in range(k)]))

binary(1,lines[-1],lines,n)
print(answer)



