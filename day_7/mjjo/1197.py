import sys
import heapq

sys.stdin = open('day_7/mjjo/1197.txt')
input = sys.stdin.readline
V, E = map(int, input().split())
visited = []
heap = []
for _ in range(E):
    A, B, C = map(int, input().split())
    heap.append([C, A-1, B-1]) # heap.append([C, A, B]) 1, 2번
heap.sort(reverse=True)
res = 0
cnt = 0

# 1
def check(node_a, node_b):
    global visited
    idx_a = -1
    idx_b = -1
    for idx, s in enumerate(visited):
        if node_a in s:
            idx_a = idx
        if node_b in s:
            idx_b = idx

    return idx_a, idx_b

while (cnt < V-1):
    link = heapq.heappop(heap)
    weight, node_a, node_b = link
    idx_a, idx_b = check(node_a, node_b)

    if (idx_a == -1) and (idx_b == -1):
        visited.append(set([node_a, node_b]))
        res += weight
        cnt += 1
    elif (idx_a == -1):
        visited[idx_b].add(node_a)
        res += weight
        cnt += 1
    elif (idx_b == -1):
        visited[idx_a].add(node_b)
        res += weight
        cnt += 1
    elif idx_a == idx_b:
        pass
    else:
        visited[idx_a] = visited[idx_a].union(visited[idx_b])
        visited.pop(idx_b)
        res += weight
        cnt += 1

print(res)


# 2
def check(node_a, node_b):
    for idx, s in enumerate(sets):
        if node_a in s:
            idx_a = idx
        if node_b in s:
            idx_b = idx

    return idx_a, idx_b

def union(idx_a, idx_b):
    sets[idx_a] = sets[idx_a].union(sets[idx_b])
    sets.pop(idx_b)

sets = [set([_]) for _ in range(1, V+1)]

while (len(sets)) > 1:
    link = heapq.pop()
    weight, node_a, node_b = link
    idx_a, idx_b = check(node_a, node_b)
    if idx_a != idx_b:
        union(idx_a, idx_b)
        res += weight

print(res)


# 3 크루스칼 알고리즘
class DisJoinSet:
    def __init__(self, n):
        self.U = []
        for i in range(n):
            self.U.append(i)

    def equal(self, p, q):
        return True if (p == q) else False

    def find(self, i):
        j = i
        while (self.U[j] != j):
            j = self.U[j]
        return j

    def union(self, p, q):
        if (p < q):
            self.U[q] = p 
        else:
            self.U[p] = q

def kruskal(n):
    cnt = 0
    res = 0
    dset = DisJoinSet(n)
    while (cnt < n-1):
        link = heap.pop()
        weight, i, j = link
        p = dset.find(i)
        q = dset.find(j)
        if (not dset.equal(p, q)):
            dset.union(p, q)
            cnt += 1
            res += weight
            print(dset.U)

    return res

print(kruskal(V))