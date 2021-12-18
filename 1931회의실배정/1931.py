from sys import stdin

n =  int(stdin.readline())
timeList = []

for i in range(n):
    startTime, endTime = map(int, stdin.readline().split())
    timeList.append((startTime,endTime))


timeList.sort(key=lambda x:(x[1],x[0]))
answer=1
finish=timeList[0][1]


for i in range(1,n):
    if timeList[i][0]<finish:continue
    answer+=1
    finish = timeList[i][1]

print(answer)
    
