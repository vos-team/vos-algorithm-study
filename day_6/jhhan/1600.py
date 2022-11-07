import sys

dx = [0,0,1,-1]
dy = [1,-1,0,0]
hx = [-1,-2,-2,-1,1,2,2,1]
hy = [-2,-1,1,2,2,1,-1,-2]

def bfs(visited):
  q = [(0,0,0,0)]
  visited[0][0][0] = True
  
  while q:
    x,y,cnt,horse_jump_cnt = q.pop(0)
    if x == N-1 and y == M-1:
      return cnt
  
    if horse_jump_cnt < K:
      # 말 점프 하는 경우
      for i in range(8):
        nx = hx[i] + x
        ny = hy[i] + y
        if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0 and not visited[nx][ny][horse_jump_cnt+1]:
          visited[nx][ny][horse_jump_cnt+1] = True
          q.append((nx, ny, cnt+1, horse_jump_cnt+1))
  
    # 말 점프 안하는 경우
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0<=nx<N and 0<=ny<M and board[nx][ny] == 0 and not visited[nx][ny][horse_jump_cnt]:
        visited[nx][ny][horse_jump_cnt] = True
        q.append((nx, ny, cnt+1, horse_jump_cnt))

  return -1

K = int(sys.stdin.readline())
M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[[False] * (K+1)  for _ in range(M)] for _ in range(N)]

print(bfs(visited))