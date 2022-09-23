from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

testCases = int(input())
for _ in range(testCases):
    n, m = map(int, input().split())
    count = 0
    scores = list(map(int, input().split()))
    queue = deque(enumerate(scores))

    while(1):
        if queue[0][1] >= max(queue, key = lambda x:x[1])[1]: 
            count += 1
            currentIdx, _ = queue.popleft()
            if(currentIdx == m):
                print(count)
                break
        else:
            queue.rotate(1)