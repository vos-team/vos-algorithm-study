# 말이 되고픈 원숭이
# 정수 K(말처럼 움직일 수 있는 횟수) 격자판 크기(가로길이 W, 세로길이 H)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

K = int(input())
C, R = map(int, input().split())

dir_monkey = [(-1,0), (1,0), (0,1), (0,-1)]
dir_horse = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

def bfs():
    need_visit = deque()
    need_visit.append((0, 0, 0, 0))

    visited = [[[False for _ in range(K + 1)] for _ in range(C)] for _ in range(R)]
    visited[0][0][0] = True
    
    while need_visit:
        row, col, depth, horse_move_count = need_visit.popleft()
        
        if row == R - 1 and col == C - 1:
            return depth
        
        move_like_monkey(row, col, depth, horse_move_count, visited, need_visit)
        if horse_move_count < K:
            move_like_horse(row, col, depth, horse_move_count, visited, need_visit)
    return -1

def is_in(row, col): 
    return 0 <= row < R and 0 <= col < C

def move_like_monkey(row, col, depth, horse_move_count, visited, need_visit):
    for dx, dy in dir_monkey:
        next_row, next_col = row + dx, col + dy
        if is_in(next_row, next_col) and board[next_row][next_col] == 0: 
            if not visited[next_row][next_col][horse_move_count]:
                visited[next_row][next_col][horse_move_count] = True
                need_visit.append((next_row, next_col, depth + 1, horse_move_count))

def move_like_horse(row, col, depth, horse_move_count, visited, need_visit):
    for dx, dy in dir_horse:
        next_row, next_col = row + dx, col + dy
        if is_in(next_row, next_col) and board[next_row][next_col] == 0:
            if not visited[next_row][next_col][horse_move_count + 1]:
                visited[next_row][next_col][horse_move_count + 1] = True
                need_visit.append((next_row, next_col, depth + 1, horse_move_count + 1))

print(bfs())