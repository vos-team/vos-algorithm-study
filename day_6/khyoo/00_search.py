import sys

node_cnt, edge_cnt, start_node = map(int, sys.stdin.readline().split())

graph = [[0] * (node_cnt + 1) for _ in range(node_cnt + 1)]

for _ in range(edge_cnt):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1


def dfs(graph, curr_node, visited, result):
    visited[curr_node] = 1
    result.append(curr_node)

    for linked_node in range(1, node_cnt + 1):
        if graph[curr_node][linked_node] and not visited[linked_node]:
            dfs(graph, linked_node, visited, result)


visited = [0] * (node_cnt + 1)
result = []
dfs(graph, start_node, visited, result)

print(" ".join(map(str, result)))

from collections import deque


def bfs(graph, start_node, visited, result):
    nodes_to_visit = deque([start_node])

    while nodes_to_visit:
        node = nodes_to_visit.popleft()

        if not visited[node]:
            visited[node] = 1
            result.append(node)

            for linked_node in range(1, node_cnt + 1):
                if graph[node][linked_node] and not visited[linked_node]:
                    nodes_to_visit.append(linked_node)


visited = [0] * (node_cnt + 1)
result = []
bfs(graph, start_node, visited, result)

print(" ".join(map(str, result)))
