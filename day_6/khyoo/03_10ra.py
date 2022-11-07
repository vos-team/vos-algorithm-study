import sys

n, m, k = map(int, sys.stdin.readline().split())


class Node:
    def __init__(self, id, parent=None):
        self.id = id
        self.parent = parent
        self.node_cnt = 1

    def get_root(self):
        root_candidate = self
        while True:
            if not root_candidate.parent:
                return root_candidate
            root_candidate = root_candidate.parent

    def __str__(self):
        return f"node_{self.id}"


board = [[-1] * (m + 2)] + [[-1] + [0] * m + [-1] for _ in range(n)] + [[-1] * (m + 2)]

trash_locs = {}
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r][c] = 1
    trash_locs[(r, c)] = Node((r, c))

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


for trash_loc in trash_locs:
    for move in moves:
        next_r, next_c = trash_loc[0] + move[0], trash_loc[1] + move[1]
        next = (next_r, next_c)
        if board[next_r][next_c] >= 0 and next in trash_locs:
            f, t = trash_locs[trash_loc], trash_locs[next]
            f_root, t_root = map(lambda n: n.get_root(), [f, t])

            if f_root != t_root:
                t_root.parent = f_root
                f_root.node_cnt += t_root.node_cnt


roots = set(map(lambda trash: trash.get_root(), trash_locs.values()))
max_nodex_root = max(roots, key=lambda root: root.node_cnt)
print(max_nodex_root.node_cnt)
