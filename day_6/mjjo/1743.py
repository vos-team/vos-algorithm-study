import sys
from collections import deque

sys.stdin = open('day_6/mjjo/1743.txt')
input = sys.stdin.readline
N, M, K = map(int, input().split())
print(N, M, K)
board = [[0]*M for _ in range(N)]
visited = [[0] for _ in range(N)]
trash_loc = [list(map(int, input().split())) for _ in range(K)]
for loc in trash_loc:
    x, y = loc
    board[x-1][y-1] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in board:
    print(_)
print(trash_loc)

def is_no_way(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<N) and (0<=ny<M) and (board[nx][ny] == 1):
            return True
    return False

def func(x, y):
    # check = [[0 for _ in range(4)] for _ in range(4)]
    d = deque()
    # check[x][y] = 0
    cnt = 0
    d.append([x, y])

    while d:
        x, y = d.popleft()
        if is_no_way(x, y):
            print('noway')
            return cnt
        for i in range(4):
            # print(check)
            nx = x+dx[i]
            ny = y+dy[i]
            print(nx, ny)
            if (0<=nx<N) and (0<=ny<M) and (board[nx][ny] == 1):
                d.append([nx, ny])
                # check[nx][ny] = check[x][y]+1
                cnt += 1
    return cnt

pts = []
for loc in trash_loc:
    print(loc)
    x, y = loc
    pt = func(x-1, y-1)
    pts.append(pt)

print(pts)

