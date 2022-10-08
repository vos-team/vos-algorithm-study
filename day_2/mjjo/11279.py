import sys
import heapq

sys.stdin = open('day_2/mjjo/11279.txt')
input = sys.stdin.readline

n = int(input().strip())
arr = list()

for i in range(n):
    req = int(input().strip())
    if req:
        heapq.heappush(arr, [-req, req])
    else:
        print(heapq.heappop(arr)[1]) if len(arr) else print(0)