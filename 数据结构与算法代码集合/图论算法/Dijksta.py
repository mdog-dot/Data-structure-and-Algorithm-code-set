# Dijkstra算法的本质就是图的BFS算法+贪心
# （贪心体现在采用优先级队列而不是一般BFS算法里的队列，让距离起点更近的节点优先出队）
import heapq
class State:
    # 当前节点ID
    def __init__(self, node:int, distFromStart:int):
        self.node = node
        # 从起点s到当前node节点的最小路径权重和
        self.distFromStart = distFromStart
    # 定义小顶堆需要的比较函数，决定了两个State类如何比较大小，在heapq构建的优先级队列中有用
    def __lt__(self, other):
        return self.distFromStart < other.distFromStart

# 输入不包含负权重边的加权图graph和起点src
# 返回从起点src到其他节点的最小路径权重和，构成一个数组
def dijkstra(graph,src: int):
    # distTo[i]表示从起点src到节点i的最小路径权重和
    distTo = [-1] * graph.size()
    # 用优先级队列代替普通BFS算法中的队列q，保证distFromStart较小的节点排在前面
    pq = []
    # 从起点src开始进行BFS
    heapq.heappush(pq, State(src,0))
    while pq:
        state = heapq.heappop(pq)
        curNode = state.node
        curDistFromStart = state.distFromStart

        if distTo[curNode] != -1:
            # 这里比图的BFS是多出来的一步，因为根据贪心算法，第一次出队的state就是对应的最小路径权重和
            continue
        # curNode 节点第一次出队时，对应于src到curNode的最小路径权重和
        # 注意这种贪心算法成立的前提是无负权重边，这样可以认为当该节点第一次出队时，他是当前可以到达路径的最小值，剩余可以到达该节点的路径都需要先经过其他节点再回到该节点，于是肯定对应更大的路径权重和
        distTo[curNode] = curDistFromStart
        for e in graph.neighbors(curNode):
            nextNode = e.to
            nextDistFromStart = curDistFromStart + e.weight
            if distTo[nextNode] == -1:
                continue
            # 和图的BFS不同，不能在入队时更新distTo，只能在出队时更新，因为只有出队时对应于最短路径，所以在Dijkstra中队列内可能存在重复节点
            heapq.heappush(pq,State(nextNode,nextDistFromStart))
    return distTo
# 输入进Dijkstra的是有向加权图
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