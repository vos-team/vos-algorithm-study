import sys

def input():
    return sys.stdin.readline().rstrip()

edges = []
parent, rank = dict(), dict()
v, e = map(int, input().split())

def make_set(node):
    parent[node] = node
    rank[node] = 0

[make_set(node) for node in range(1, v+1)]

for i in range(e):
    node_a, node_b, weight = map(int, input().split())
    edges.append((weight, node_a, node_b))

def union(node_a, node_b):
    root_a, root_b = find(node_a), find(node_b)
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else: 
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
            
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]
    
def kruskal(edges):
    result = 0
    for edge in sorted(edges):
        weight, node_a, node_b = edge
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            result += weight
    return result 

print(kruskal(edges))