from sys import stdin

n, k = map(int, stdin.readline().split())

# 물병의 개수를 K개 이하의 2의 제곱수의 합으로 나타낼 수 있어야 한다
# 물병의 개수 = bin(n).count('1')
ans = 0
while bin(n).count('1') > k:
    # 제일 끝에 있는 1을 하나 올려준다
    plus = 2 ** bin(n)[::-1].index('1')
    ans += plus
    n += plus

print(ans)