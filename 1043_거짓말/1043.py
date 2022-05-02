from sys import stdin

# 분리 집합

# 파티, 참가자 정보 입력
n, m = map(int, stdin.readline().split())
knows = set(map(int, stdin.readline().split()[1:])) # 진실을 아는 사람들
parties = []
for _ in range(m):
    parties.append(set(map(int, stdin.readline().split()[1:])))

# 매 파티마다 진실을 알게 되는 사람이 새로 생길 수 있으므로, 파티 수만큼 반복해야 한다.
for _ in range(m):
    for party in parties:
        # 파티 잠여자 중 진실을 아는 사람이 있으면 union
        if party & knows:
            knows = knows | party

cnt = 0
for party in parties:
    if party & knows:
        continue
    # 파티 참가자와 진실을 아는 사람의 교집합이 없을 때만 거짓말을 할 수 있다.
    cnt += 1

print(cnt)

