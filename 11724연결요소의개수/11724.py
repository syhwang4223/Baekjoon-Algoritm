from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

st = []
chk = [False for _ in range(n+1)]
ans = 0

for i in range(1,n+1):
    if chk[i]:
        continue
    ans += 1
    st.append(i)
    while st:
        cur = st.pop()
        for nxt in graph[cur]:
            if not chk[nxt]:
                st.append(nxt)
                chk[nxt] = True

print(ans)
               

    
