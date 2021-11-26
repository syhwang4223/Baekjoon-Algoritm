from sys import stdin

def binary(arr, target, start, end):
    global answer

    if start>end:
        return 

    mid = (start+end)//2 #절단기의 높이 H
    total = 0 #잘린 나무의 길이의 합
    for tree in trees:
        if tree>mid:
            total += tree-mid

    #잘린 나무의 길이가 필요한 나무의 길이보다 크거나 같다
    if total>=target:
        answer = mid
        binary(arr,target,mid+1,end)
        
    #잘린 나무의 길이가 필요한 나무의 길이보다 작다
    else:
        binary(arr,target,start,mid-1)

n,m = map(int, stdin.readline().split())
trees = sorted(map(int, stdin.readline().split()))
answer = 0

binary(trees,m,0,trees[-1])
print(answer)
