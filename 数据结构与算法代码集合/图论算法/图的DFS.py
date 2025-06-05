# 图结构和多叉树结构非常类似，唯一的区别在于图的一个节点可以有出去的也可以有进来的，因此图结构中可能存在环，在遍历时要注意避免成环
# 遍历图的所有节点(visited数组)
# 这里直接调用graph图对象的API（邻接表和邻接矩阵共用相同的API）
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

graph = WeightedDigraph()

# s是即将遍历的节点序号，visited用于存放已经遍历的节点
visited =  [False] * len(graph) # 一开始所有节点都没有遍历过
def traverse(graph, s, visited):
    if s < 0 or s >= len(graph):
        return
    if visited[s]:
        # 防止成环
        return 
    # 前序位置
    visited[s] = True
    print('visit', s)
    for e in graph.neibors(s):
        traverse(graph, e.to, visited)
    # 后序位置

# 遍历图的所有路径（onPath数组） 寻找从src到dest的所有路径
# 需要注意onPath数组和遍历节点的visited数组的不同之处在于，它们本身的作用都是在遍历的路上防止遍历到
# 已遍历过的节点导致成环无限循环，但由于onPath要保证能寻找到所有路径，而不同路径之间可能有重合的节点
# 因此onPath在遍历完退出节点后需要撤销标记。（和多叉树的遍历本质是一样的，但是由于存在防止成环引入on_path数组，故后序需要撤销访问标记）
onPath = [False] * len(graph)
path = []

def traverse(graph, src, dest):
    if src < 0 or src >= len(graph):
        return
    if onPath[src]:
        # 防止成环
        return
    onPath[src] = True
    path.append(src)
    if src == dest:
        print(f'find path: {path}')
    for e in graph.neighbors(src):
        traverse(graph, e.to, dest)
    # 后序位置：应该在遍历完退出节点后撤销标记
    onPath[src] = False
    path.pop()
