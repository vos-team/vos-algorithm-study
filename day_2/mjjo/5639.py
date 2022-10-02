import sys

sys.setrecursionlimit(10**6)
sys.stdin = open('day_2/mjjo/5639.txt')
input = sys.stdin.readline

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None

# class BinarySearchTree(object):
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         self.root = self._insert_value(self.root, data)
#         return self.root is not None

#     def _insert_value(self, node, data):
#         if node is None:
#             node = Node(data)
#         else:
#             if data <= node.data:
#                 node.left = self._insert_value(node.left, data)
#             else:
#                 node.right = self._insert_value(node.right, data)
#         return node

#     def pre_order(self):
#         def _pre_order(root):
#             if root is None:
#                 pass
#             else:
#                 print(root.data)
#                 _pre_order(root.left)
#                 _pre_order(root.right)
#         _pre_order(self.root)

#     def post_order(self):
#         def _post_order(root):
#             if root is None:
#                 pass
#             else:
#                 _post_order(root.left)
#                 _post_order(root.right)
#                 print(root.data)
#         _post_order(self.root)

# sys.stdin = open('day_2/mjjo/5639.txt')
# input = sys.stdin.readline

# bst = BinarySearchTree()

# while True:
#     try:
#         bst.insert(int(input().strip()))
#     except:
#         break

# bst.post_order()


# 2
# def to_post(pre_order):
#     length = len(pre_order)

#     if length <= 1:
#         return pre_order
    
#     for i in range(1, length):
#         if pre_order[i] > pre_order[0]: # pre_order root(0번째)보다 큰 수가 나올 경우
#             return to_post(pre_order[1:i]) + to_post(pre_order[i:]) + [pre_order[0]]

#     return to_post(pre_order[1:]) + [pre_order[0]] 

# pre_order = []
# while True:
#     try:
#         pre_order.append(int(input().strip()))
#     except:
#         break

# post_order = to_post(pre_order)
# for _ in post_order:
#     print(_)


# 3
pre_order = []

def to_post(start, end):
    if start >= end:
        return

    root = pre_order[start] # 전위 순회에서 첫번째 값이 root

    if pre_order[end - 1] <= root: # pre_order 마지막 값이 root보다 작으면 (left만 있을 경우)
        to_post(start + 1, end) # left만 하면 됨, start + 1은 root를 제외
        print(root) # root print
        return

    for i in range(start + 1, end): # root보다 큰 값을 찾아서 left, right를 나누기 위한
        if pre_order[i] > root:
            idx = i # left, right를 구분할 인덱스 설정
            break
    
    # 후위 순회이기 때문에 left, right, print(root) 순으로 처리
    to_post(start + 1, idx)
    to_post(idx, end)
    print(root)

while True:
    try:
        pre_order.append(int(input()))
    except:
        break

to_post(0, len(pre_order))


# 처리 진행

# stpe 1
# [50, 30, 24, 5, 28, 45, 98, 52, 60]
# start 0, end 9
# root [50]
# idx 6
# left [30, 24, 5, 28, 45]
# right [98, 52, 60]

# step 2
# start 1, end 6
# [30, 24, 5, 28, 45] left가 먼저 처리되므로
# root [30]
# idx 5
# left [24, 5, 28]
# right [45]

# step 3
# start 2, end 5
# [24, 5, 28]
# root [24]
# idx 4
# left [5]
# right [28]

# step 4
# start 3, end 4
# [5]
# root [5]
# if pre_order[end - 1] <= root: 이므로 to_post(start + 1, end) 이므로
# print root

# step 5 가장 마지막 right가 실행
# start 4, end 5
# [28]
# root [28]
# if pre_order[end - 1] <= root: 이므로 to_post(start + 1, end) 이므로
# print root

# ... 반복