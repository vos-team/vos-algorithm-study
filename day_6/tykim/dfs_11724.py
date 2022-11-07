from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())

graph = defaultdict(list)

visited = list(0 for _ in range(n+1))

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())

    graph[x].append(y)
    graph[y].append(x)

count = 0

def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)