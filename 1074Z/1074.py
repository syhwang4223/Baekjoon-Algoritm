from sys import stdin

n,r,c = map(int,stdin.readline().split())
global ans
ans = 0

def devide(n,r,c):
    global ans
    if n==1:
        ans+=2*r+c
        return    
    #왼쪽 위
    if r<2**(n-1) and c<2**(n-1):
        devide(n-1,r,c)
    #오른쪽 위
    elif r<2**(n-1):
        ans+=(4**(n-1))
        devide(n-1,r,c-2**(n-1))
    #왼쪽 아래
    elif c<2**(n-1):
        ans+=2*(4**(n-1))
        devide(n-1,r-2**(n-1),c)
    #오른쪽 아래
    else:
        ans+=3*(4**(n-1))
        devide(n-1,r-2**(n-1),c-2**(n-1))

devide(n,r,c)
print(ans)
