import sys

# 0123 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
snake_dir = 1 
snake_pos_queue = [[0,0]]

# ----------------------------------------
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

board = list([0]*n for _ in range(n))
board[0][0] = 2 # 내 몸통

for i in range(k):
  x,y = map(int, sys.stdin.readline().split())
  board[x-1][y-1] = 1
  
l = int(sys.stdin.readline())

dir_dict = dict()
for i in range(l):
  time, dir = sys.stdin.readline().split()
  dir_dict[int(time)] = dir
  
time = 0
while 1:
  # 뱀의 머리 전진
  hx, hy = snake_pos_queue[-1][0] + dx[snake_dir], snake_pos_queue[-1][1] + dy[snake_dir]
  # 벽에 부딪혔나요?
  if hx < 0 or hx > n-1 or hy <0 or hy >n-1:
    break
  
  get_apple = False
  if board[hx][hy] == 1:   # 사과가 있나요?
    get_apple = True
  elif board[hx][hy] == 2: # 내 몸통인가요?
    break
  
  if not get_apple :
    # 꼬리를 큐에서 꺼내서 버리고 board 비우기
    tx,ty = snake_pos_queue.pop(0)
    board[tx][ty] = 0
  
  # 새로운 머리를 큐에 넣고 지도에 표시
  snake_pos_queue.append([hx,hy])
  board[hx][hy] = 2
  
  # 시간 증가
  time +=1
  
  # time 초 끝나고 방향 변경
  if time in dir_dict :
    snake_dir = snake_dir-1 if dir_dict[time] == 'L' else snake_dir+1
  if snake_dir <0: snake_dir = 3
  if snake_dir >3: snake_dir = 0
    
print(time+1)