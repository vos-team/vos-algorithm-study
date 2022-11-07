from collections import deque, defaultdict
import sys

# import numpy

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())

board = []
for _ in range(h):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)


class Move:
    def __init__(self, directions):
        self.directions = directions

    def get_next_possible_locs(self, board, curr_loc):
        next_possible_locs = []
        for direction in self.directions:
            dy, dx = direction
            y, x = curr_loc
            next_loc = (y + dy, x + dx)
            if not board[next_loc[0] + 1][next_loc[1] + 1]:
                next_possible_locs.append(next_loc)
        return next_possible_locs


class Game:
    def __init__(self, board, monkey_move: Move, horse_move: Move, k, w, h):
        self.board = self.pad_board(board)
        self.monkey_move = monkey_move
        self.horse_move = horse_move
        self.k = k
        self.w = w
        self.h = h
        self.visited_board = defaultdict(lambda: 0)

    def pad_board(self, board):
        h_padding = [[1] * (w + 4)] * 2
        w_padding = [1] * 2
        padded_board = h_padding + []
        for row in board:
            padded_board.append(w_padding + row + w_padding)
        padded_board += h_padding
        return padded_board

    def solution(self):
        init_loc = (1, 1)
        init_horse_power_left = self.k
        init_state = (init_loc, init_horse_power_left)
        self.visited_board[init_state] = 0

        end_loc = (self.h, self.w)

        states_to_visit = deque([init_state])

        while states_to_visit:
            curr_state = states_to_visit.popleft()
            curr_loc, curr_horse_power_left = curr_state

            if curr_loc == end_loc:
                return self.visited_board[curr_state]

            if curr_horse_power_left:
                for next_loc in horse_move.get_next_possible_locs(self.board, curr_loc):
                    next_state = (next_loc, curr_horse_power_left - 1)
                    if not self.visited_board[next_state]:
                        self.visited_board[next_state] = (
                            self.visited_board[curr_state] + 1
                        )
                        states_to_visit.append(next_state)

            for next_loc in monkey_move.get_next_possible_locs(self.board, curr_loc):
                next_state = (next_loc, curr_horse_power_left)
                # print(curr_state, next_state)
                if not self.visited_board[next_state]:
                    self.visited_board[next_state] = self.visited_board[curr_state] + 1
                    states_to_visit.append(next_state)
        return -1


monkey_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
monkey_move = Move(monkey_directions)

mul = lambda t1, t2: (t1[0] * t2[0], t1[1] * t2[1])
signs = ((1, 1), (1, -1), (-1, 1), (-1, -1))
horse_directions = sum(
    ([mul(direction, sign) for sign in signs] for direction in ((1, 2), (2, 1))), []
)
horse_move = Move(horse_directions)

game = Game(board=board, monkey_move=monkey_move, horse_move=horse_move, k=k, w=w, h=h)

print(game.solution())
