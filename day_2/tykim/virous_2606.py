import sys

# 컴퓨터의 수
n = int(sys.stdin.readline().strip())

# 연결된 컴퓨터 쌍의 수
m = int(sys.stdin.readline().strip())

# 직접 연결되어있는 컴퓨터 쌍
connected = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())		
    connected[x].append(y)
    connected[y].append(x)

# 재귀함수를 통해서 방문처리를 진행
visited = [False] * (n + 1) # 방문 boolean 초기화

count = 0

def dfs(connected, v, visited):
    global count
    visited[v] = True
    count +=1

    for i in connected[v]:
        
        if visited[i] == False:
            
            dfs(connected, i, visited)


dfs(connected, 1, visited)

print(count -1)

