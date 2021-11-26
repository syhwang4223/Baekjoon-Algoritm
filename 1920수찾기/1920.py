
from sys import stdin,stdout

n = int(stdin.readline())
A = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
B = map(int,stdin.readline().split())


def search(target, arr, start, end):
    if start>end:
        return 0
    mid = (start+end)//2

    if arr[mid]==target:
        return 1
    elif arr[mid]>target:
        return search(target,arr,start,mid-1)
    else:
        return search(target,arr,mid+1,end)


for target in B:
    print(search(target,A,0,n-1))
    
