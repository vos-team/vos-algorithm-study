# 사과를 먹으면 꼬리가 늘어남
# 사과가 없으면 몸길이 그대로
# 자기 자신을 나타내는 상태값 필요  
from collections import deque


dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

n = int(input())
k = int(input())

# 보드 크기 초기화
board = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 2 # 사과 위치

turns = dict()
for _ in range(int(input())):
    s, d = input().split()
    turns[int(s)] = 1 if d == "D" else -1

curr_sec = 0
x, y, d = 0, 0, 0
snake = deque([(0, 0)])
board[0][0] = 1

while True:
    curr_sec += 1
    x, y = x + dx[d], y + dy[d]

    if not (0 <= x < n) or not (0 <= y < n) or (board[x][y] == 1):
        break

    if board[x][y] == 0:
        snake.append((x, y))
        board[x][y] = 1
        a, b = snake.popleft()
        board[a][b] = 0
    # 이동한 칸에 사과 있을 때
    elif board[x][y] == 2:
        snake.append((x, y))
        board[x][y] = 1

    if curr_sec in turns:
        d = (d + turns[curr_sec]) % 4

print(curr_sec)