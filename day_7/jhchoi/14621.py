
import sys

def input():
    return sys.stdin.readline().rstrip()

edges = []

parent, rank = dict(), dict()

def make_set(node):
    parent[node] = node
    rank[node] = 0


n, m = map(int, input().split())

univ = input().split()

[make_set(node) for node in range(1, n + 1)]

total_distance = 0

for i in range(m):
    u, v, distance = map(int, input().split())
    edges.append((distance, u, v))
    total_distance += distance

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
            rank[root_a] += 1

def kruskal(edges):
    mst_weight = 0
    cnt = 0
    edges.sort()

    for weight, node_a, node_b in edges:
        if univ[node_a - 1] != univ[node_b - 1]:
            if find(node_a) != find(node_b):
                union(node_a, node_b)
                mst_weight += weight
                cnt += 1
    return mst_weight, cnt


mst_weight, cnt = kruskal(edges)

if cnt != n - 1:
    print(-1)
else:
    print(mst_weight)