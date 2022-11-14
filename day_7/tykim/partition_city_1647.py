import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parent(parent, x):

    if parent[x] != x:
        return find_parent(parent, parent[x])

    else:
        return x

def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


n, m = map(int, input().split())
# 서로소 집합 확인하는 리스트
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, cost = map(int,input().split())

    edges.append((cost, a, b))

edges.sort()

roads = []
road_cost = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        road_cost += cost
        roads.append(cost)

roads.pop()
final_cost = 0
for x in roads:
    final_cost += x

print(final_cost)