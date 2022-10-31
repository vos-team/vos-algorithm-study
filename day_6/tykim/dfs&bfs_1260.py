from collections import deque
from collections import defaultdict

n, m, v = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


node = v

# 받은 값을 키값을 중심으로 정렬해주기
graph = dict(zip(graph.keys(), map(lambda x: sorted(x, key=int), graph.values())))

# dfs 함수
def dfs(graph, node, visited):
    
    # 주어진 시작점이 없을때
    if node not in graph:
        print(node, end = " ")
        return

    stack = [node]

    cur = stack.pop()

    if cur in visited: 
        return
    
    visited.add(cur)
    print(cur, end = " ")
    
    for next in graph[cur]:
        dfs(graph, next, visited)

# bfs 함수
def bfs(graph, node, visited):

    # 주어진 시작점이 없을때
    if node not in graph:
        print(node, end = " ")
        return
    queue = deque([node])
    visited = set([node])

    while queue:
        cur = queue.popleft()
        
        print(cur, end = " ")
        
        for next in graph[cur]:
            if next in visited: 
                continue
                
            queue.append(next)
            visited.add(next)



dfs(graph, node, set()) 
print() # end를 " "로 지정했기때문에 띄어쓰기를 위해서 print문 넣어주기
bfs(graph, node, set())
