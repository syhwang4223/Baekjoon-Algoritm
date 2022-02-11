from sys import stdin

def dfs(pick_cnt, idx):

    # 6개의 번호를 전부 뽑았을 경우 출력
    if pick_cnt == 6:
        print(*picked)
        return

    #그렇지 않은 경우, S의 뒷부분을 탐색하며
    for i in range(idx, k):
        # 번호 하나를 새롭게 뽑는다
        picked.append(S[i])
        dfs(pick_cnt + 1, i + 1)
        # 취소한다
        picked.pop()


while True:
    tmp = list(map(int, stdin.readline().split()))
    k = tmp[0]
    if k == 0:
        break
    S = tmp[1:]
    
    picked = []
    dfs(0,0)
    print()
