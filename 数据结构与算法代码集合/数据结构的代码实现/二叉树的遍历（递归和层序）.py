# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 二叉树的遍历框架
# 递归遍历（DFS）是使用函数堆栈实现的遍历，traverse的遍历顺序是一直往左子节点走，直到遇到空指针不能再走了
# 才尝试往右子节点走一步，然后再一直尝试往左子节点走，如此循环，直到左右子树都走完了，才返回上一层
# 父节点，递归遍历的顺序仅取决于左右子节点的递归调用顺序（即先traverse.left还是traverse.right)，
# 与其他代码无关，只要调用顺序不变，访问节点的顺序就不变，但访问顺序不变不代表读取节点值或执行其他命令
# 的顺序固定，这与命令的位置有关，由此引出了前序、中序、后序遍历
def traverse(root: TreeNode):
    if root is None:
        return
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历

# 前序、中序、后序遍历分别对应代码块放在前中后三个不同位置，前序即访问到哪就先执行代码块，执行顺序与访问顺序相同
# 中序即在左子树遍历完后再执行，后序即在左右子树都遍历完后再执行，因此读取节点值的顺序有三种

# 二叉树的层序遍历：需要借助队列实现（BFS）
from collections import deque
def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # 记录当前遍历到的层数（根节点是第一层）
    depth = 1
    while len(q) > 0:
        sz = len(q)
        # 引入sz是为了判断当前层是否遍历完，因为q中还会不断加入新的节点，当前层遍历完时队列不是空
        # i标记了当前层的第几个节点
        for i in range(sz):
            cur = q.popleft() # 注意deque的popleft方法在删除元素时，还会返回删除掉的元素
            print(f"depth = {depth}, val = {cur.val}")
            # 把cur的左右子节点加入队列
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
            # 一层遍历完之后剩下的q就是下一层的所有节点，于是实现层序遍历
        depth += 1

# 二叉树的层序遍历还可以引申出更高要求
# 上面的层序遍历记录了节点所在的深度，如果把每条路径的权重定义为1，则深度depth=root权重+路径权重和
# 假如我们认为不同路径的权重是不同值，那么同一层节点的权重值就不一定相等了，这时就需要记录每个节点
# 的路径权重和，通过添加一个类State，让每个节点自己维护自己的权重和

class State:
    def __init__(self, node: TreeNode, depth: int):
        self.node = node
        self.depth = depth
        
def levelOrderTraversewithWeight(root):
    if root is None:
        return
    q = deque()
    # 根节点路径权重和为1
    q.append(State(root, 1))
    
    while len(q) > 0:
        cur = q.popleft()
        print(f"depth = {cur.depth}, val = {cur.node.val}")
        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + 1))
# 上面这种方法每个节点都有自己对应的depth，最为灵活，但比起一般的层序遍历略显麻烦

