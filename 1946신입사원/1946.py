from sys import stdin
import heapq

def testcase():
    n = int(input())
    grades = []
    cnt = 1
    for _ in range(n):
        a,b = map(int, stdin.readline().split())
        grades.append((a,b))
    grades.sort(key = lambda x:x[0])
  
    m = grades[0][1] #첫사람의 인터뷰 점수
    for paper, interview in grades:
        if interview<m:
            cnt+=1
            m = interview
    print(cnt)
        
    
t = int(input())
for _ in range(t):
    testcase()
