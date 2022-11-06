import sys

sys.stdin = open('day_7/mjjo/1647.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
heapq = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.append([C, A-1, B-1])
heapq.sort(reverse=True)

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
    while (cnt < n-2):
        link = heapq.pop()
        weight, i, j = link
        p = dset.find(i)
        q = dset.find(j)
        if (not dset.equal(p, q)):
            dset.union(p, q)
            cnt += 1
            res += weight
    return res

print(kruskal(N))