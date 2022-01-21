from sys import stdin

m = int(input())
s = [False for _ in range(21)]

for _ in range(m):
    command = list(stdin.readline().split())
    if len(command)>=2:
        x = int(command[1])

    if command[0] == "all":
        s = [True for _ in range(21)]
    elif command[0] == "empty":
        s = [False for _ in range(21)]
    
    elif command[0] == "add":
        s[x] = True
    elif command[0] == "check":
        print(1 if s[x] else 0)
    elif command[0] == "toggle":
        s[x] = not s[x]
    else:#remove
        s[x] = False
