import sys

def dfs(cur, visited):
  print(cur, end=" ")
  visited[cur] = True
  for next in g[cur]:
    if not visited[next]:
      dfs(next, visited)

def bfs(start, visited):
  queue = [start]
  visited[start] = True
  while queue:
    cur = queue.pop(0)
    print(cur, end=" ")
    for next in g[cur]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)
  

N,M,V = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N+1)]

for i in range(M):
  x,y = map(int, sys.stdin.readline().split())
  g[x].append(y)
  g[y].append(x)

for i in g:
  i.sort()

dfs(V, [False]*(N+1))
print('')
bfs(V, [False]*(N+1))