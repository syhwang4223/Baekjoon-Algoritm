from sys import stdin

st = []

k = int(stdin.readline())
for i in range(k):
    num = int(stdin.readline())
    if num>0:
        st.append(num)
    else:
        st.pop()
ans = 0
for n in st:
    ans+=n
    
print(ans)
