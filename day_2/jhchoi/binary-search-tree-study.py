class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.__insertValue(self.root, data)
        return self.root is not None
    
    def __insertValue(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.__insertValue(node.left, data)
            else: 
                node.right = self.__insertValue(node.right, data)
        return node

    def find(self, key):
        return self.__findValue(self.root, key)

    def __findValue(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.__findValue(root.left, key)
        else: 
            return self.__findValue(root.right, key)

    def preorder(self):
        self.__preorder(self.root)

    def __preorder(self, root):
        if not root: return
        print(root.data, end = ' ')
        self.__preorder(root.left)
        self.__preorder(root.right)
    
    def inorder(self):
        self.__inorder(self.root)

    def __inorder(self, root):
        if not root: return
        self.__inorder(root.left)
        print(root.data, end = ' ')
        self.__inorder(root.right)

    def postorder(self):
        self.__postorder(self.root)
    
    def __postorder(self, root):
        if not root: return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data, end = ' ')

array = [50, 30, 24, 45, 5, 28, 98, 52, 60]
bst = BST()
for x in array:
    bst.insert(x)

bst.preorder()
print()
bst.inorder()
print()
bst.postorder()
