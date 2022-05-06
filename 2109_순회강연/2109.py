from sys import stdin
import heapq

# 우선순위 큐

n = int(stdin.readline())
lectures = []

# 강연 조건 입력
for _ in range(n):
    p, d = map(int, stdin.readline().split())
    lectures.append((p, d))

# 강연일이 가까운 강연 순으로 정렬
lectures.sort(key=lambda x: x[1])

hq = []

for p, d in lectures:
    heapq.heappush(hq, p)

    # 힙의 크기가 강연을 해야하는 날짜보다 크면 모든 강연을 못하므로 제일 페이가 작은 강의를 버린다
    if len(hq) > d:
        heapq.heappop(hq)


print(sum(hq))
