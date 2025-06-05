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
if __name__ == "__main__":
    graph = WeightedDigraph(3)
    graph.addEdge(0, 1, 1)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 0, 3)
    graph.addEdge(2, 1, 4)

    print(graph.hasEdge(0, 1))  # true
    print(graph.hasEdge(1, 0))  # false
