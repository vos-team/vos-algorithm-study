# 1
import sys

class Stack:
    def __init__(self):
        self.arr = list()

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.arr.__len__():
            print(self.arr.pop())
        else:
            print(-1)

    def size(self):
        print(self.arr.__len__())

    def empty(self):
        if self.arr.__len__():
            print(0)
        else:
            print(1)

    def top(self):
        if self.arr.__len__():
            print(self.arr[-1])
        else:
            print(-1)


n = int(input())

stack = Stack()
for _ in range(n):
    req = sys.stdin.readline().strip()
    if 'push' in req:
        x = int(req.split(' ')[1])
        stack.push(x)
    elif 'pop' == req:
        stack.pop()
    elif 'size' == req:
        stack.size()
    elif 'empty' == req:
        stack.empty()
    elif 'top' == req:
        stack.top()
    else:
        raise(ValueError)


# 2
import sys

n = int(input())
stack = list()

for _ in range(n):
    req = sys.stdin.readline().strip()
    if 'pop' == req:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif 'size' == req:
        print(len(stack))
    elif 'empty' == req:
        if len(stack):
            print(0)
        else:
            print(1)
    elif 'top' == req:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(int(req.split(' ')[-1]))