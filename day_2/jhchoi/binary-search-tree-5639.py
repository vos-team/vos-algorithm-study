import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

preorder = []

def postorder(rootIndex, endIndex):
    if rootIndex > endIndex: return 
    root = preorder[rootIndex]

    rightIndex = endIndex + 1
    for i in range(rootIndex + 1, endIndex + 1):
        if preorder[i] > root:
            rightIndex = i
            break

    postorder(rootIndex + 1, rightIndex - 1)   
    postorder(rightIndex, endIndex)
    print(root)


data = input()
while(data):
    preorder.append(int(data))
    data = input()

postorder(0, len(preorder) - 1)