# 并查集的本质在模型层面上是把点集之间的连接关系用一颗树来表示出来，相连的节点由其共同的根节点来代表
# 在数据结构层面上，可以用一个表示每个节点的父节点的数组parent来表征
# 并查集的时间复杂度取决于树高，因此并查集实现的关键在于如何压缩树高，一个很聪明的方法是在find方法往上寻找根节点的过程中将每个父节点都递归地指向根节点
class UF:
    def __init__(self, n):
        self._count = n
        self.parent = [i for i in range(1, n + 1)]
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return
        self.parent[rootQ] = rootP
        self._count -= 1
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
    def count(self):
        return self._count
    
    # 关键在于find函数如何高效找到该节点的根节点
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # 个人感觉有点像二叉树的前序遍历
        return self.parent[x]
            
        