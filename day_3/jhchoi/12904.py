import sys

def input():
    return sys.stdin.readline().rstrip()

s = list(input())
t = list(input())

result = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        result = True
        break

print(1) if result else print(0)