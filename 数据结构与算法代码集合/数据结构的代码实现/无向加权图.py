# 无向加权图就等同于有双向的有向加权图
# 可以直接在有向加权图的前提下对增删改查分别补上对称的操作
# 有向加权图的通用实现（邻接表）
# 存储相邻节点及边的权重
class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight
class WeightedDigraph:
    def __init__(self, n):
        # 这里简单起见，建图时要传入总结点数，
        # 可以通过Map优化做到动态添加新节点
        self.graph = [[] for _ in range(n)]
    # 增，添加一条有权重的有向边，O（1）
    def addEdge(self, from_, to, weight):
        self.graph[from_].append(Edge(to, weight))
    # 删，删除一条有向边，复杂度O（V）,V为节点个数
    def removeEdge(self, from_, to):
        self.graph[from_] = [e for e in self.graph if e.to != to]
    
    # 查，判断两个节点是否相邻，复杂度O(V)
    def hasEdge(self, from_, to):
        for e in self.graph[from_]:
            if e.to == to:
                return True
        return False
    # 查，返回一条边的权重，复杂度O(V)
    def weight(self, from_, to):
        for e in self.graph[from_]:
            if e.to == to:
                return e.weight
        raise ValueError("No such edge")
    # 查，返回某个节点的所有邻居节点，复杂度O（1）
    def neighbors(self, from_):
        return self.graph[from_]

class WeightedUndigraph:
    def __init__(self, n):
        self.graph = WeightedDigraph(n)

    # 增，添加一条带权重的无向边
    def addEdge(self, frm, to, weight):
        self.graph.addEdge(frm, to, weight)
        self.graph.addEdge(to, frm, weight)

    # 删，删除一条无向边
    def removeEdge(self, frm, to):
        self.graph.removeEdge(frm, to)
        self.graph.removeEdge(to, frm)

    # 查，判断两个节点是否相邻
    def hasEdge(self, frm, to):
        return self.graph.hasEdge(frm, to)

    # 查，返回一条边的权重
    def weight(self, frm, to):
        return self.graph.weight(frm, to)

    # 查，返回某个节点的所有邻居节点
    def neighbors(self, v):
        return self.graph.neighbors(v)