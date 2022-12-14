import sys

def bfs(start, visited):
  queue = [start]
  visited[start] = True
  while queue:
    cur = queue.pop(0)
    for next in g[cur]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)

N,M = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
  u,v = map(int, sys.stdin.readline().split())
  g[u].append(v)
  g[v].append(u)

link_count = 0
for cur in range(1, N+1):
  if not visited[cur]:
    link_count +=1
    bfs(cur, visited)
print(link_count)

