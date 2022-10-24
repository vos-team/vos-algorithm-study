from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

apples = [tuple(map(int, stdin.readline().split())) for _ in range(K)]

L = int(stdin.readline())

moves = [(int(X), C) for X, C in (stdin.readline().split() for _ in range(L))]


def matmul(rot, direction):
    return (
        rot[0][0] * direction[0] + rot[0][1] * direction[1],
        rot[1][0] * direction[0] + rot[1][1] * direction[1],
    )


def solution(N, apples, moves):
    class snake:
        def __init__(self, board):
            self.head = (1, 1)
            self.direction = (0, 1)
            self.length = 1
            self.body = [self.head]
            self.board = board
            for part in self.body:
                board[part[0]][part[1]] = -1
            self.rotation = {
                "L": ((0, -1), (1, 0)),
                "D": ((0, 1), (-1, 0)),
            }

        def proceed(self):
            # new_head = tuple(np.array(self.head) + self.direction)
            new_head = (
                self.head[0] + self.direction[0],
                self.head[1] + self.direction[1],
            )
            if self.board[new_head[0]][new_head[1]] == -1:
                return False

            if self.board[new_head[0]][new_head[1]] == 1:
                self.length += 1
            else:
                self.board[self.body[0][0]][self.body[0][1]] = 0

            self.head = new_head
            self.board[self.head[0]][self.head[1]] = -1
            self.body.append(self.head)
            self.body = self.body[-self.length :]
            return True

        def rotate(self, C):
            # self.direction = np.matmul(self.rotation[C], self.direction)
            self.direction = matmul(self.rotation[C], self.direction)

    # board = np.zeros((N + 2, N + 2))
    # board[[0, N + 1]] = -1
    # board[:, [0, N + 1]] = -1
    board = (
        [[-1] * (N + 2)] + [[-1] + [0] * N + [-1] for _ in range(N)] + [[-1] * (N + 2)]
    )
    for apple_y, apple_x in apples:
        board[apple_y][apple_x] = 1

    s = snake(board)
    result = 1
    while s.proceed():
        if len(moves):
            X, C = moves[0]

            if X == result:
                s.rotate(C)
                moves = moves[1:]
        result += 1
    return result


print(solution(N, apples, moves))
