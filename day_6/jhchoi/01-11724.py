# 11724 - 연결 요소의 개수
# 정점의 개수 N / 간선의 개수 M
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = {n: [] for n in range(1, N+1)}
visited = {n: False for n in range(1, N + 1)}
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start_node):
    if visited[start_node]: 
        return
    need_visit = [start_node]

    while need_visit:
        curr_node = need_visit.pop()
        if not visited[curr_node]:
            visited[curr_node] = True
            need_visit.extend(graph[curr_node])
        
for curr_node in range(1, N+1):
    if not visited[curr_node]:
        dfs(graph, curr_node)
        cnt += 1
print(cnt)