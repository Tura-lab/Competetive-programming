class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        
        for a, b, w in edges:
            self.graph[a].append((b, w))

    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        self.graph[a].append((b, w))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        visited = set()
        q = [(0, node1)]
        while q:
            cost, node = heappop(q)
            
            if node == node2:
                return cost
            
            visited.add(node)
            for v, w in self.graph[node]:
                if v not in visited:
                    heappush(q, (cost + w, v))
            
        return -1
            
        
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)