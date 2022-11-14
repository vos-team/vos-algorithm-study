import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

parent, rank = dict(), dict()
edges = []

def make_set(node):
    parent[node] = node
    rank[node] = 0

[make_set(node) for node in range(1, n+1)]

for _ in range(m):
    node_a, node_b, weight = map(int, input().split())
    edges.append((weight, node_a, node_b))

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_a, node_b):
    root_a, root_b = find(node_a), find(node_b)
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def kruskal(edges):
    edges.sort()
    result = []
    for weight, node_a, node_b in edges:
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            result.append(weight)
    return result

# 마을 두개로 나눠야 하니까 weight이 가장 큰 마지막 인덱스 제외하고 출력
print(sum(kruskal(edges)[:-1]))