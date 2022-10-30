import sys

node_cnt, edge_cnt = map(int, sys.stdin.readline().split())


class Node:
    def __init__(self, id, parent=None):
        self.id = id
        self.parent = parent

    def get_root(self):
        root_candidate = self
        while True:
            if not root_candidate.parent:
                return root_candidate
            root_candidate = root_candidate.parent

    def __str__(self):
        return f"node_{self.id}"


nodes = {i: Node(i) for i in range(1, node_cnt + 1)}

for _ in range(edge_cnt):
    n1, n2 = map(lambda n: nodes[int(n)], sys.stdin.readline().split())
    n1_root, n2_root = map(lambda n: n.get_root(), [n1, n2])

    if n1_root != n2_root:
        n2_root.parent = n1_root

print(len(set(map(lambda node: node.get_root(), nodes.values()))))
