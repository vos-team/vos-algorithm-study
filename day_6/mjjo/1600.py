import sys

sys.stdin = open('day_6/mjjo/1600.txt')
input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
check = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]
horse_x = [1, 1, 2, 2, -1, -1, -2, -2]
horse_y = [2, -2, 1, -1, 2, -2, 1, -1]
monkey_x = [0, 0, 1, -1]
monkey_y = [1, -1, 0, 0]
dx = monkey_x + horse_x
dy = monkey_y + horse_y

def bfs(spx, spy, cnt):
    able = False
    queue = []
    check[spy][spx][cnt] = 0
    queue.append([spx, spy, cnt])

    while queue:
        x, y, c = queue.pop(0)
        if x == W-1 and y == H-1:
            print(check[y][x][c])
            able = True
            break
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<W and 0<=ny<H and board[ny][nx] != 1:
                if i < 4:
                    if check[ny][nx][c] == False:
                        check[ny][nx][c] = check[y][x][c] + 1
                        queue.append([nx, ny, c])
                else:
                    if c < K and check[ny][nx][c+1] == False:
                        check[ny][nx][c+1] = check[y][x][c] + 1
                        queue.append([nx, ny, c+1])

    if able == False:
        print(-1)

bfs(0, 0, 0)
