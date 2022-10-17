N = int(input())

stack = []

order = list(input().split() for i in range(N))

for i in range(N):
    if order[i][0] == "push":
        stack.append(int(order[i][1]))
    
    elif order[i][0] == "pop":
        if stack != []:
            print(stack.pop())
        else:
            print(-1)
    
    elif order[i][0] == "size":
        print(len(stack))
        
    elif order[i][0] == "empty":
        if stack != []:
            print(0)
        else:
            print(1)
            
    elif order[i][0] == "top":
        if stack != []:
            print(stack[-1])
        else:
            print(-1)