import sys,collections

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

isReversed = False
count = len(t) - len(s)
queue = collections.deque(t)

while count :
    pop = queue.popleft() if isReversed else queue.pop()
    if pop == 'B':
        isReversed = not isReversed
    count -=1

result = ''.join(reversed(queue) if isReversed else queue)
print(1 if s == result else 0)