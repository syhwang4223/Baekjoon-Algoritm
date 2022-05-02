from sys import stdin



def testcase():
    # 하나의 테스트 케이스 에 대한 로직

    # 문제에 노드의 최대 번호 수에 대한 정보가 없네
    tree = [[] for i in range(14)]
    nodes = set()  # 존재하는 모든 노드 번호

    while True:
        tmp = list(map(int, stdin.readline().split()))
        for i in range(0, len(tmp), 2):
            u, v = tmp[i], tmp[i + 1]
            if u != 0 or v != 0:
                # print(u, v)
                tree[v].append(u)  # tree[i] : i의 부모 노드
                # print(tree[v])

                nodes.add(u)
                nodes.add(v)

            else:
                # 한 테스트 케이스 에 대한 입력이 끝남
                # print(tree[:maxi + 1])

                # 부모 노드가 없는 노드가 단 하나 존재 해야 한다.
                # 그 외의 모든 노드는 부모가 하나 씩 존재 해야 한다.
                cnt = 0
                for node in nodes:
                    # print(node, tree[node])
                    if len(tree[node]) > 1:
                        return False
                    elif len(tree[node]) == 0:
                        cnt += 1
                        if cnt > 1:
                            return False
                return True


k = 1
while True:
    tf = testcase()
    if tf:
        print("Case " + str(k) + " is a tree.")
    else:
        print("Case " + str(k) + " is not a tree.")


    eof = stdin.readline().rstrip()
    if eof == "-1 -1":
        break


    k += 1


