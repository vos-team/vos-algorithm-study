import sys
sys.setrecursionlimit(20000)

# dfs 탐색
def dfs(start, end):
    # 시작과 끝 값이 역전시 리턴
    if start > end: return
    temp = end + 1
    # 서브 트리 찾기
    for i in range(start + 1, end + 1):
        # 루트 보다 크면 오른쪽 서브 트리
        if graph[start] < graph[i]:
            temp = i
            break

    dfs(start + 1, temp - 1) # 왼쪽 서브 트리 재귀적으로 탐색
    dfs(temp, end) # 오른쪽 서브 트리 재귀적으로 탐색
    print(graph[start])

graph = []
for n in sys.stdin:
  graph.append(int(n.rstrip()))
dfs(0, len(graph) - 1)


# !시간초과 발생
# 노드 객체 만든 버전
# import sys
# sys.setrecursionlimit(10**9)

# class Node: 
#   def __init__(self, num):
#     self.num = num
#     self.left = None
#     self.right = None
  
#   def add_left(self, Node):
#     self.left = Node
    
#   def add_right(self, Node):
#     self.right = Node
  

# def insert(placed_node, node):
#   if node < placed_node.num:
#     if placed_node.left is None :
#       placed_node.left = Node(node)
#     else :
#       insert(placed_node.left, node)
#   else :
#     if placed_node.right is None :
#       placed_node.right = Node(node)
#     else :
#       insert(placed_node.right, node)
  

# def post_order(node):
#   if node.left : post_order(node.left)
#   if node.right : post_order(node.right)
#   print(node.num)

# root = Node(int(sys.stdin.readline().rstrip()))
# for n in sys.stdin:
#   insert(root, int(n.rstrip()))

# post_order(root)


# !시간초과 발생
# 노드 객체가 아니라 왼/오른쪽만 list(tuple(왼, 오)) 로 저장
# import sys
# sys.setrecursionlimit(20000)

# tree = [(None, None)] * 1000001

# def insert(parent, node):
#   left, right = tree[parent]
#   if node < parent:
#     if left: insert(left, node)
#     else: tree[parent] = (node,right)
#   else:
#     if right: insert(right, node)
#     else: tree[parent] = (left, node)
  

# def post_order(node):
#   left, right = tree[node]
#   if left : post_order(left)
#   if right : post_order(right)
#   print(node)

# root = int(sys.stdin.readline().rstrip())
# for n in sys.stdin:
#   insert(root, int(n.rstrip()))

# post_order(root)