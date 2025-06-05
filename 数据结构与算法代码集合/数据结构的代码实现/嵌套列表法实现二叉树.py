def BinaryTree(r):
    return [r,[],[]]
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        # 如果本来有值，就把本来的树接在这后面，这种方法每次只能把子树加在root后面
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
def getRootval(root):
    return root[0]
def setRootval(root,newval):
    root[0] = newval
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertRight(r,5)
insertLeft(r[1],6)
insertLeft(r,7)
print(r)
