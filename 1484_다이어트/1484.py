from sys import stdin

# 최소 스패닝 트리 (MST) : 간선들의 가중치 합이 최소인 신장 트리
# 스패닝(신장) 트리 : 모든 정점을 잇지만, 사이클이 없는 부분 그래프. e = v - 1

# 크루스칼 알고리즘
#   그리디 알고리즘. 모든 간선에 대해 정렬을 수행 한 뒤, 가장 비용이 작은 간선부터 집합에 포함시킨다.
# 1. 간선 비용 오름차순으로 정렬
# 2. 간선을 하나씩 확인
#   1) 사이클이 발생하지 않는 경우 MST 에 포함시킨다.
#   2) 사이클이 발생하는 경우 MST 에 포함시키지 않는다.
# 3. 모든 간선에 대해 2 의 과정을 반복


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    m, n = map(int, stdin.readline().split())
    if m == 0 and n == 0:
        break

    # 테스트 케이스 별 그래프 정보 입력
    costs = []
    for i in range(n):
        x, y, z = map(int, stdin.readline().split())
        costs.append([x, y, z])

    # 간선 비용 정렬
    costs.sort(key=lambda c: c[2])
    # 부모 노드 초기화
    parent = [i for i in range(m)]

    ans = 0
    # 간선을 하나씩 확인
    for x, y, z in costs:
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
        else:
            ans += z

    print(ans)



    