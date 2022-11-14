import sys

def input():
    return sys.stdin.readline().rstrip()

# 특정 원소가 속한 집합 찾는법:
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속해있으면 합치기
def union_parent(parent, a, b):
    # 각각의 루트번호를 찾아주기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 큰쪽을 찾아서 작은쪽의 루트 노드로 지정해주는것
    if a < b:
        parent[b] = a

    else:
        parent[a] = b

# 정점과 간선을 받아주기
v, e = map(int, input().split())

parent = [0] * (v+1)

# 부모 노드를 알기 위해 초기화 시켜주기
for i in range(1, v+1):
    parent[i] = i

edges = []
final_cost = 0
# e개의 줄에는 간선에 대한 정보가 나타남
for i in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 원소를 비용으로 적용
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        final_cost += cost
    
print(final_cost)
