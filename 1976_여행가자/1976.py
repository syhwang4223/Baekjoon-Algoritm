from sys import stdin

# union - find
# 분리 집합 (disjoint set)

n = int(stdin.readline())
m = int(stdin.readline())
graphs = []
parent = [i for i in range(n)]

# 그래프 정보 입력
for _ in range(n):
    graphs.append(list(map(int, stdin.readline().split())))

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 떄까지 재구적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# union-find
for i in range(n):
    for j in range(n):
        # 두 도시가 연결되어 있으면 부모 노드 바꿔주기
        if graphs[i][j] == 1:
           union_parent(parent, i, j)
        
# 여행할 도시 순서 입력
travel = list(map(int, stdin.readline().split()))
# 연결 되어 있으면 부모 노드가 같다
parent_list = []
for t in travel:
    parent_list.append(parent[t-1])

if len(set(parent_list)) == 1:
    print("YES")
else:
    print("NO")