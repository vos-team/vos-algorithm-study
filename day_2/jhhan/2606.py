import sys, collections

def bfs(start, size, arr):
  visited = [False] * size
  visited[start] = True
  queue = collections.deque([start])
  count = 0 # 1번 컴퓨터는 제외함
  
  while queue :
    cur = queue.pop()
    for node in arr[cur]:
      if not visited[node]:
        visited[node] = True
        queue.append(node)
        count +=1
  return count

n = int(sys.stdin.readline().rstrip())
link_count = int(sys.stdin.readline().rstrip())

links = [[] for i in range(n)]

for i in range(link_count):
  a, b = list(map(int, sys.stdin.readline().split()))
  links[a-1].append(b-1)
  links[b-1].append(a-1)
  
ans = bfs(0, n, links)
print(ans)