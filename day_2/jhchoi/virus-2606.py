import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(graph, root):
    visited = []
    queue = deque([root])
    visited.append(root)
    while(queue):
        node = queue.popleft()
        pairNodes = graph.get(node)
        for pairNode in pairNodes:
            if pairNode not in visited:
                visited.append(pairNode)
                queue.append(pairNode)
    return visited

numberOfComputers = int(input())
pairNumber = int(input())
graph = {}

for i in range(1, numberOfComputers + 1):
    graph[i] = set()

for _ in range(1, pairNumber + 1):
    i, j = map(int, input().split())
    graph[i].add(j)
    graph[j].add(i)

visited = bfs(graph, 1)
print(len(visited) - 1)