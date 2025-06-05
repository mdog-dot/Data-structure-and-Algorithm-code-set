class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight
class WeightedDigraph:
    def __init__(self, n):
        # 邻接矩阵 matrix[from][to]存储从节点from到节点to的边的权重，0表示没有连接
        self.matrix = [[0] * n for _ in range(n)]
    # 增，添加一条带权重的有向边，复杂度O(1)
    def addEdge(self, from_, to, weight):
        self.matrix[from_][to] = weight
    # 删，删除一条有向边，复杂度O（1）
    def removeEdge(self, from_, to):
        self.matrix[from_][to] = 0
    # 查，判断两个节点相邻
    def hasEdge(self, from_, to):
        if self.matrix[from_][to] != 0:
            return True
        return False
    # 查，返回一条边的权重，复杂度O(1)
    def weight(self, from_, to):
        return self.matrix[from_][to]
    # 查，返回某个节点的所有邻居节点，复杂度O(V)
    def neighbors(self, from_):
        neighbor = []
        for i in range(len(self.matrix)):
            if self.matrix[from_][i] != 0:
                neighbor.append(Edge(i, self.matrix[from_][i]))
        return neighbor

    
