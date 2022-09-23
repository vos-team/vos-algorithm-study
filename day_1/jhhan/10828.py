import sys

n = int(sys.stdin.readline().rstrip())
stack = []

for i in range(n):
  commands = sys.stdin.readline().split()
  com = commands[0]
  if com == 'push':
    stack.append(commands[1])
  elif com == 'pop':
      print(stack.pop() if len(stack) else -1)
  elif com == 'size':
    print(len(stack))
  elif com == 'empty':
    print(0 if len(stack) else 1)
  elif com == 'top':
    print(stack[-1] if len(stack) else -1)
