import sys
import heapq
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())  # 정점 수, 간선 수

graph = defaultdict(list)  # 빈 그래프 생성

visited = [0] * (n + 1)  # 정점의 방문 정보 초기화

# 그래프에 간선정보 받기
for _ in range(k):
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])


construct_graph = defaultdict(list)

# 프림 알고리즘
def prim(graph, start_node):
    # 시작점에 방문 표시
    visited[start_node] = 1
    # 인접 간선을 우선순위 큐로 만들어주기
    candidate = graph[start_node]
    heapq.heapify(candidate)
    # mst이면 넣어줄 리스트 생성
    mst = []
    # 최종 비용 산출을 위해 만들어주기
    final_cost = 0

    while candidate:
        # heappop을 활용해서 비용이 가장 적은 간선 추출
        weight, u, v = heapq.heappop(candidate)
        if visited[v] == 0:  # 방문하지 않았다면
            visited[v] = 1  # 방문 갱신
            # mst에 넣어주기
            mst.append((u, v))
            # 비용 더해주기
            final_cost += weight
            construct_graph[u].append((-weight, u, v))
            construct_graph[v].append((-weight, v, u))

            # 다음 인접 간선을 탐색하고 방문한 정점이 아니라면(순환 방지) 우선 순위 큐에 값 넣어주기
            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)
    return final_cost


print(prim(graph, 1))
# print(graph)
# print(construct_graph)

dp_arr = [[0] * n for _ in range(n)]
# dp_arr = [0] * n


def get_max_cost(visited, curr_cost, start, end, construct_graph):
    if dp_arr[start][end] < 0:
        return dp_arr[start][end]
    if dp_arr[end][start] < 0:
        return dp_arr[end][start]

    next_nodes = sorted(construct_graph[start])
    heapq.heapify(next_nodes)

    while next_nodes:
        next_node = heapq.heappop(next_nodes)
        next_cost, _, next_node_idx = next_node

        if not visited[next_node_idx]:
            visited[next_node_idx] = 1
            if next_node_idx == end:
                return curr_cost + next_cost
            else:
                return get_max_cost(
                    visited, curr_cost + next_cost, next_node_idx, end, construct_graph
                )

    return 0


for u in range(n):
    for v in range(u + 1, n):
        if u != v:
            # print(u, v)
            visited = [0] * n
            visited[u] = 1
            # print(get_max_cost(visited, 0, u, v, construct_graph))
            dp_arr[u][v] = -get_max_cost(visited, 0, u, v, construct_graph)

print(max(sum(dp_arr, [])))
