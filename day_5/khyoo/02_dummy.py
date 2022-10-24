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
                board[part[0]][part[1]] = -1  # 뱀의 몸체가 위치한 좌표는 -1 표시
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
                return False  # 나아간 곳이 -1이면 죽음

            if self.board[new_head[0]][new_head[1]] == 1:
                self.length += 1  # 나아간 곳이 1이면(사과) 몸길이 1증가
            else:
                self.board[self.body[0][0]][
                    self.body[0][1]
                ] = 0  # 나아간 곳에 사과가 없으면 꼬리(index=0) 좌표 0으로 되돌림

            self.head = new_head  # 살아있으면 new_head를 머리로 지정
            self.board[self.head[0]][self.head[1]] = -1  # 추가된 머리의 죄표에 해당하는 보드판을 -1로 변경
            self.body.append(self.head)  # self.body 에 머리 추가
            self.body = self.body[-self.length :]  # 현재 몸길이만큼 self.body 슬라이싱
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
    # 보드판 정의(N+2 * N+2) 크기로 만들고 테두리는 -1, 안쪽 N*N 영역은 0으로 채워둠

    for apple_y, apple_x in apples:
        board[apple_y][apple_x] = 1
    # 사과 좌표마다 1로 채워둠

    s = snake(board)

    result = 1
    while s.proceed():  # 1초 앞으로 나가면서 시작

        if len(moves):
            X, C = moves[0]

            if X == result:
                s.rotate(C)
                moves = moves[1:]
        result += 1
    return result


print(solution(N, apples, moves))
