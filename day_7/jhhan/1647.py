import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
edges = []
parent = [0] * (v+1)
total_cost = []

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total_cost.append(cost)

total_cost.sort()
print(sum(total_cost[:-1]))