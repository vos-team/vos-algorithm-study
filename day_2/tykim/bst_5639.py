import sys

sys.setrecursionlimit(10**9)

def postorder(left,right):
    if left > right:
        return
    else:
        root=tree[left]
        div = right+1

        for i in range(left+1,right+1):
            if root<tree[i]: 
                div = i
                break
            
        postorder(left+1, div-1)
        postorder(div, right)
        print(root)
    
tree=[]
while True:
    try:
        tree.append(int(sys.stdin.readline().strip()))

    except:
        break

postorder(0,len(tree)-1)
