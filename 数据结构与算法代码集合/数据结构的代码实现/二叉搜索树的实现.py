class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    def _put(self, key, val, root: TreeNode):
        if key < root.key:
            if root.hasLeftChild():
                self._put(key, val, root.leftChild)
            else:
                root.leftChild = TreeNode(key, val, parent=root)
        elif key > root.key:
            if root.hasRightChild():
                self._put(key, val, root.rightChild)
            else:
                root.rightChild = TreeNode(key, val, parent=root)
        else:
            root.payload = val
    def get(self, key, root: TreeNode):
        if root is None:
            return None
        if key == root.key:
            return root
        if key < root.key:
            return self.get(key, root.leftChild)
        if key > root.key:
            return self.get(key, root.rightChild)
    def __getitems__(self, key: TreeNode):
        return self.get(key, self.root).payload
    
    # 最复杂的在于删除操作
    def delete(self, key):
        if not self.get(key, self.root):
            raise KeyError("Key is not in Tree")
        target = self.get(key, self.root)
        if self.size == 1:
            self.root = None
        else:
            self.remove(target)
        self.size -= 1
    def remove(self, target: TreeNode):
        # 分为三种情况考虑
        # 第一种情况是被删节点无子节点
        if target.leftChild is None and target.rightChild is None:
            if target.isLeftChild():
                target.parent.leftChild = None
            if target.isRightChild():
                target.parent.rightChild = None
        # 第二种情况是被删节点有一个子节点，将子节点接入被删节点的位置即可
        elif target.hasLeftChild() and not target.hasRightChild():
            if target.isLeftChild():
                target.parent.leftChild = target.leftChild
            elif target.isRightChild():
                target.parent.rightChild = target.leftChild
            else:
                # target是根节点
                self.root = target.leftChild
                self.root.parent = None
        elif target.hasRightChild() and not target.hasLeftChild():
            if target.isLeftChild():
                target.parent.leftChild = target.rightChild
            elif target.isRightChild():
                target.parent.rightChild = target.rightChild
            else:
                # target是根节点
                self.root = target.rightChild
                self.root.parent = None
        # 第三种情况是被删节点有两个子节点，可以选取被删节点右子树中最小的节点接入别删节点的位置
        else:
            succ = self.getMin(target.rightChild)
            succ.parent.leftChild = None
            succ.parent = target.parent
            succ.leftChild = target.leftChild
            succ.rightChild = target.rightChild
            if target.isLeftChild():
                target.parent.leftChild = succ
            if target.isRightChild():
                target.parent.rightChild = succ
    
    # 尝试对上面的delete方法做出改进
    # 令delNode返回根节点节点删除key节点之后的根节点（对应删过以后的子树）
    def delNode(self, key, root: TreeNode):
        if root is None:
            raise KeyError("Key is not in Tree")
        if key == root.key:
            if not root.hasLeftChild():
                return root.rightChild
            if not root.hasRightChild():
                return root.leftChild
            succ = self.getMin(root.rightChild)
            root.rightChild = self.delNode(succ.key, root.rightChild)
            succ.leftChild = root.leftChild
            succ.rightChild = root.rightChild
            return succ
        if key < root.key:
            root.leftChild = self.delNode(key, root.leftChild)
        if key > root.key:
            root.rightChild = self.delNode(key, root.rightChild)
        return root    
    def getMin(self, root):
        if root.leftChild is None:
            return root
        return self.getMin(root.leftChild)
if __name__  == "__main__":
    Tree = BinarySearchTree()
    Tree.put(4,"a")
    Tree.put(2,"b")
    Tree.put(1,"c")
    Tree.put(3,"d")
    Tree.put(5,"e")
    Tree.put(-1,"f")
    Tree.delNode(2,Tree.root)
    print(Tree.root.leftChild.payload)  