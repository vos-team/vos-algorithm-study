
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

direction = [(0,-1), (0,1), (-1,0), (1,0)]

n, m, k = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(m)] # board[col][row] 
visited = [[False for _ in range(n)] for _ in range(m)] # visited[col][row]
need_visit = deque()

for _ in range(k):
    r, c = map(int, input().split())
    board[c-1][r-1] = 1

def is_in_board(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs(start_x, start_y):
    trash_count = 1
    visited[start_x][start_y] = True
    
    need_visit.append((start_x, start_y))
    
    while need_visit:
        x, y = need_visit.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if is_in_board(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                need_visit.append((nx, ny))
                trash_count += 1
    return trash_count

max_trash_count = 0

for c in range(m):
    for r in range(n):
        if board[c][r] == 1:
            max_trash_count = max(bfs(c, r), max_trash_count)
print(max_trash_count)