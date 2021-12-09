from sys import stdin

n = int(stdin.readline())
stack = []

for i in range(n):
    command = stdin.readline().split()
    if command[0]=="push":
        stack.append(command[1])
    elif command[0]=="top" and stack:
          print(stack[-1])
    elif command[0]=="top":
        print(-1)
    elif command[0]=="pop" and stack:
        print(stack.pop())
    elif command[0]=="pop":
        print(-1)
    elif command[0]=="size":
        print(len(stack))
    else:
        if not stack :print(1)
        else: print(0)
