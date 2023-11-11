class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.distances = [[float('inf')] * n for _ in range(n)]
        self.n = n
        
        for a, b, w in edges:
            self.distances[a][b] = w
        
        for i in range(n):
            self.distances[i][i] = 0
            
        self.floyd_warshal()
        
    def floyd_warshal(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.distances[i][j] = min(self.distances[i][j], self.distances[i][k] + self.distances[k][j])

    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        if w >= self.distances[a][b]:
            return
        
        self.distances[a][b] = w
        for i in range(self.n):
            for j in range(self.n):
                self.distances[i][j] = min(self.distances[i][j], self.distances[i][a] + self.distances[a][b] + self.distances[b][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        ans = self.distances[node1][node2]
        return ans if ans < float('inf') else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)