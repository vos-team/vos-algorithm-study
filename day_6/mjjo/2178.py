import sys

sys.stdin = open('day_6/mjjo/2178.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
board = [[int(_) for _ in input().strip()] for _ in range(N)]
check = [[0 for _ in range(101)] for _ in range(101)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sp = [0, 0]
ep = [N, M]

def dfs(sp, ep):
    queue = []
    queue.append(sp)
    check[sp[0]][sp[1]] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<N) & (0<=ny<M):
                if (board[nx][ny] == 1) & (check[nx][ny] == 0):
                    queue.append([nx, ny])
                    check[nx][ny] = check[x][y]+1
                    if (nx == ep[0]) & (ny == ep[1]):
                        break
    return check[ep[0]-1][ep[1]-1] +1

print(dfs(sp, ep))