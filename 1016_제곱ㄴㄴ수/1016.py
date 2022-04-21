from sys import stdin
from math import sqrt
from math import ceil

a, b = map(int, stdin.readline().split())
chk = [False for _ in range(a, b+1)] # a부터 b까지의 수들이 제곱 ㄴㄴ수인지 아닌지
squares = [i**2 for i in range(2, int(sqrt(b)) + 1)]

# max 보다 작거나 같은 모든 제곱수 들에 대해
for square in squares:
    j = ceil(a / square) # min 보다 큰, 제곱수의 배수 중 가장 작은 수
    while square * j <= b:
        chk[square * j - a] = True
        j += 1


print(chk.count(False))
