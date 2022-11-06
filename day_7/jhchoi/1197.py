import sys

def input():
    return sys.stdin.readline().rstrip()

vertices = set()
edges = []

v, e = map(int, input().split())

for i in range(e):
    node_a, node_b, weight = map(int, input().split())
    vertices.add(node_a)
    vertices.add(node_b)
    edges.append((weight, node_a, node_b))
parent, rank = dict(), dict()

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
    
def make_set(node):
    parent[node] = node
    rank[node] = 0
    
def kruskal(vertices, edges):
    result = []
    for node in vertices:
        make_set(node)
    
    for edge in sorted(edges):
        weight, node_a, node_b = edge
        
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            result.append(edge)
    return result 


mst = kruskal(vertices, edges)
count = 0
for weight, node_a, node_b in mst:
    count += weight
print(count)
    