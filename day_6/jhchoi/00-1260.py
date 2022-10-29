from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def bfs(graph, start_node):
    visited = {n: False for n in range(1, N+1)}
    result = []
    need_visit = deque()
    
    need_visit.append(start_node)
    
    while need_visit:
        curr_node = need_visit.popleft()
        if not visited[curr_node]:
            visited[curr_node] = True
            result.append(curr_node)
            need_visit += graph[curr_node]
    return result

def dfs(graph, start_node):
    need_visit, result = [], []
    visited = {n: False for n in range(1, N+1)}
    need_visit.append(start_node)
    
    while need_visit:
        curr_node = need_visit.pop()
        if not visited[curr_node]:
            visited[curr_node] = True
            result.append(curr_node)
            need_visit += reversed(graph[curr_node])
    return result

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
graph = {n: [] for n in range(1, N+1)}

for _ in range(M):
    N1, N2 = map(int, input().split())
    graph[N1].append(N2)
    graph[N2].append(N1)
    
for key in range(1, N + 1):
    graph[key].sort()
    
print(*dfs(graph, V))
print(*bfs(graph, V))