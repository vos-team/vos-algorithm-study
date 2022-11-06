import sys

def input():
    return sys.stdin.readline().rstrip()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

roads = []
for _ in range(m):
    a, b, cost = map(int,input().split())
    roads.append((cost, a, b))

roads.sort()

save_cost = 0
whole_cost = 0

for road in roads:

    cost, a, b = road

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

        save_cost += cost

    whole_cost += cost


if len(set(parent)) >= 3:
    for road in roads:

        cost, a, b = road

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)


if len(set(parent)) < 3:
    print(whole_cost-save_cost)
else:
    print(-1)

