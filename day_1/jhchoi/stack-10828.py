import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack = []
for n in range(N): 
    command = input().split()
    if(command[0] == 'push'):
        stack.append(int(command[1]))
    elif(command[0] == 'pop'):
        print(-1 if len(stack) == 0 else stack.pop())
    elif(command[0] == 'size'):
        print(len(stack))
    elif(command[0] == 'empty'): 
        print(1 if len(stack) == 0 else 0)
    elif(command[0] == 'top'): 
        print(-1 if len(stack) == 0 else stack[-1])