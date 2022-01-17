#주어진 숫자 X를 2진수로 변환했을 때 1이 몇개인가를 묻는 문제
#몇개의 2의 배수를 더하여 만들 수 있는가.

x = int(input())
ans = 0

while (x>0):
    ans+=x%2
    x//=2

print(ans)
