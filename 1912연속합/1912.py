from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

partsum = [0 for i in range(n)]
partsum[0] = arr[0]


for i in range(1,n):
    partsum[i] = max(arr[i], partsum[i-1]+arr[i])

print(max(partsum))
