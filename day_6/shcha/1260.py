from collections import deque

N, M, start = list(map(int, input().split()))

#인접영행렬
matrix= [[0]*(N+1) for i in range(N+1)]

#방문한 곳 기록용 리스트
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)


for i in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[a][b]=1


def dfs(start):
    visited_dfs[start] = 1
    print(start, end=' ')
    for i in range(1, N+1):
        if(visited_dfs[i]==0 and matrix[start][i]==1):
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = 1
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in range(1, N+1):
            if(visited_bfs[i]==0 and matrix[start][i]==1):
                  queue.append(i)
                  visited_bfs[i] = 1

dfs(start)
print()
bfs(start)
