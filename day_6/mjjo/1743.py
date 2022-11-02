import sys
from collections import deque

sys.stdin = open('day_6/mjjo/1743.txt')
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
visited = [[True]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_cnt = 0

def bfs(x, y):
    cnt = 1
    queue = deque([[x, y]])
    visited[x][y] = False

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<N) and (0<=ny<M) and (board[nx][ny]) and (visited[nx][ny]):
                visited[nx][ny] = False
                queue.append([nx, ny])
                cnt += 1
    return cnt

for _ in range(K):
    x, y = map(lambda x: int(x)-1, input().split())
    board[x][y] = 1

for x in range(N):
    for y in range(M):
        if (board[x][y]) and (visited[x][y]):
            cnt = bfs(x, y)
            max_cnt = max(max_cnt, cnt)

print(max_cnt)