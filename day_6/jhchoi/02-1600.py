import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

K = int(input())
W, H = map(int, input().split())

board = [] # board[Row][Col]
[board.append(list(map(int, input().split()))) for _ in range(H)]

dir_monkey = [(-1,0), (1,0), (0,1), (0,-1)]
dir_horse = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

# visited[Row][Col][HorseMoveCnt]
visited = [[[False for _ in range(K + 1)] for _ in range(W)] for _ in range(H)] 
need_visit = deque([(0,0,0,0)]) # row, col, depth, horse_move_cnt

def bfs():
    while need_visit:
        row, col, depth, horse_move_cnt = need_visit.popleft()
        
        if row == H - 1 and col == W - 1:
            return depth
        
        move_like_monkey(row, col, depth, horse_move_cnt)
        if horse_move_cnt < K:
            move_like_horse(row, col, depth, horse_move_cnt)
    return -1
            
def is_in_board(col, row):
    return 0 <= col < W and 0 <= row < H

def move_like_monkey(row, col, depth, horse_move_cnt):
    for dc, dr in dir_monkey:
        next_dc, next_dr = col + dc, row + dr
        if is_in_board(next_dc, next_dr) and board[next_dr][next_dc] == 0:
            if not visited[next_dr][next_dc][horse_move_cnt]:
                visited[next_dr][next_dc][horse_move_cnt] = True
                need_visit.append((next_dr, next_dc, depth + 1, horse_move_cnt))

def move_like_horse(row, col, depth, horse_move_cnt):
    for dc, dr in dir_horse:
        next_dc, next_dr = col + dc, row + dr
        if is_in_board(next_dc, next_dr) and board[next_dr][next_dc] == 0:
            if not visited[next_dr][next_dc][horse_move_cnt + 1]:
                visited[next_dr][next_dc][horse_move_cnt + 1] = True
                need_visit.append((next_dr, next_dc, depth + 1, horse_move_cnt + 1))
                
print(bfs())