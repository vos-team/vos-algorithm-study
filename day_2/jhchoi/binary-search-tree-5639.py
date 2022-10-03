import sys

def input():
    return sys.stdin.readline().rstrip()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.__insert(self.root, data)
    
    def __insert(self, root, data):
        if not root:
            root = Node(data)
        else:
            if data <= root.data:
                root.left = self.__insert(root.left, data)
            else:
                root.right = self.__insert(root.right, data)
        return root

    def postorder(self):
        self.__postorder(self.root)

    def __postorder(self, root):
        if not root: return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data)

bst = BinarySearchTree()

data = input()
while(data):
    bst.insert(int(data))
    data = input()

bst.postorder()