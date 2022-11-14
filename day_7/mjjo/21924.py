import sys

sys.stdin = open('day_7/mjjo/21924.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
total_price = 0
heapq = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.append([C, A-1, B-1])
    total_price += C
heapq.sort(reverse=True)
dset = [_ for _ in range(N)]
cnt = 0
res = 0

def is_equal(p, q):
    return True if (p == q) else False

def do_find(j):
    while dset[j] != j: # 부모노드를 계속해서 탐색
        j = dset[j]
    return j

def do_union(p, q):
    if (p < q):
        dset[q] = p 
    else:
        dset[p] = q
try:
    while (cnt < N-1):
        link = heapq.pop()
        weight, i, j = link
        p = do_find(i)
        q = do_find(j)
        if (not is_equal(p, q)):
            do_union(p, q)
            cnt += 1
            res += weight
    print(total_price - res)
except: # IndexError: pop from empty list 더이상 heapq에서 pop할 값이 없어서 indexError가 발생함
    print(-1)
