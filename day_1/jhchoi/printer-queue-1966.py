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
        currentIdx, currentScore = queue.popleft()
        if(len(queue) == 0):
            print(count+1)
            break
        if currentScore >= max(queue, key = lambda x:x[1])[1]: 
            count += 1
            if(currentIdx == m):
                print(count)
                break
        else:
            queue.append((currentIdx, currentScore))