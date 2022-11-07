import sys


sys.stdin = open('day_6/mjjo/1260.txt')
input = sys.stdin.readline
N, M, V = map(int, input().split())
# print(N, M, V)
node_dic = dict((idx, set([])) for idx in range(1,N+1))
for _ in range(M):
    m, s = map(int, input().split())
    node_dic[m].add(s)
    node_dic[s].add(m)
node_dic = dict((k, sorted(v)) for k, v in node_dic.items())

def bfs(v):
    visited = [V]
    queue = list(node_dic[v])

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue = queue + list(node_dic[node])

    return ' '.join(map(str, visited))

def dfs(v):
    visited = [V]
    queue = list(node_dic[v])

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue = list(node_dic[node]) + queue

    return ' '.join(map(str, visited))

print(dfs(V))
print(bfs(V))
