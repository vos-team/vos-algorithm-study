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


n, m = map(int, sys.stdin.readline().split())
edges = []
parent = [0] * (n+1)
total_cost = 0
total_edges_cost = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
    total_edges_cost += cost

edges.sort()

for i in range(m):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        total_cost += cost

all_connected = True
for i in range(2, n+1):
    if find_parent(parent, 1) != find_parent(parent, i):
        all_connected = False
        break
    
print(total_edges_cost-total_cost if all_connected else -1)