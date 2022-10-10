import sys
from collections import defaultdict

getLine = lambda: sys.stdin.readline().strip()

v_cnt = int(getLine())
e_cnt = int(getLine())

graph = defaultdict(dict)
for _ in range(e_cnt):
    v1, v2 = getLine().split()
    graph[v1][v2] = True
    graph[v2][v1] = True

infected = set(("1"))
visited = set()


def investigate(v):
    visited.add(v)
    for linked_v in graph[v]:
        infected.add(linked_v)
        if linked_v not in visited:
            investigate(linked_v)


investigate("1")
print(len(infected) - 1)
