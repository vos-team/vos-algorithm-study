import sys

sys.setrecursionlimit(10**6)

# 풀이 1 -> 시간초과
getNum = lambda: int(sys.stdin.readline().strip())


class Node:  # 노드 구현
    def __init__(self, num, parent):
        self.num = num
        self.parent = parent
        self.left = None
        self.right = None


class Tree:  # 트리 기능 구현
    def __init__(self, root):
        self.root = root

    def add(self, num):  # 트리에 새로운 숫자 넣을 때 로직 구현
        curr_node = self.root

        while True:
            if curr_node.num < num:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    new_leaf = Node(num, curr_node)
                    new_leaf.num = num
                    curr_node.right = new_leaf
                    break

            if curr_node.left:
                curr_node = curr_node.left
            else:
                new_leaf = Node(num, curr_node)
                curr_node.left = new_leaf
                break

    def backward(self):  # 문제에서 원하는 backward 출력 구현
        if self.root:
            curr_node = self.root
            printed = set()
            while True:
                if curr_node.left and curr_node.left.num not in printed:
                    curr_node = curr_node.left
                elif curr_node.right and curr_node.right.num not in printed:
                    curr_node = curr_node.right
                else:
                    print(curr_node.num)
                    printed.add(curr_node.num)
                    if curr_node.parent:
                        curr_node = curr_node.parent
                    else:
                        break


# root = Node(getNum(), None)
# tree = Tree(root)

# while True:
#     try:
#         tree.add(getNum())
#     except:
#         break

# tree.backward()


# 풀이 2 -> 통과긴 한데 메모리 많이 사용
# forward_tree = list(
#     int(line) for line in sys.stdin.read().splitlines()
# )  # 전체 숫자 입력 리스트로 받아옴


def backward_tree(forward_tree):
    if len(forward_tree) <= 1:  # 서브트리 전위순회 리스트의 길이가 1개 이하면 바로 리턴
        return forward_tree
    else:  # 서브트리 전위순회 리스트의 길이가 2개 이상이면, 맨 앞 루트와 서브트리로 나눠서 재귀 돌림
        root = forward_tree[0]

        if (
            forward_tree[-1] < root
        ):  # 서브트리 전위순회 리스트 맨 마지막 원소가 루트보다 작으면 루트 하위의 오른쪽 서브트리는 없음
            i = len(forward_tree)
        else:  # 루트보다 큰 원소 나타날 때 까지 찾아서 해당 원소부터는 루트 하위 오른쪽 서브트리로
            for i in range(len(forward_tree)):
                if forward_tree[i] > root:
                    break

        left_subtree = forward_tree[1:i]
        right_subtree = forward_tree[i:]
        return backward_tree(left_subtree) + backward_tree(right_subtree) + [root]


# result = backward_tree(forward_tree)
# for i in range(len(result)):
#     print(result[i])


# 풀이 3

forward_tree = tuple(int(line) for line in sys.stdin.read().splitlines())


def backward_tree(start, end):
    if start == end:
        return

    root = forward_tree[start]
    if end - start == 1:
        return print(root)

    if root > forward_tree[end - 1]:
        bp = end
    else:
        bp = start
        for i in range(start, end):
            if forward_tree[i] > root:
                bp = i
                break

        if bp == start:
            bp = i + 1

    backward_tree(start + 1, bp)
    backward_tree(bp, end)
    print(root)


backward_tree(0, len(forward_tree))
