class UnionFind:
    def __init__(self, n):
        self.parents = {i+1:i+1 for i in range(n)}
        self.rank = {i+1:1 for i in range(n)}
        
    def find(self, v):
        if self.parents[v] == v:
            return v
        return self.find(self.parents[v])
    
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
    
        if p1 == p2:
            return True
        
        if self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]
            
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for v1,v2 in edges:
            n = max(n,v1,v2)
            
        uf = UnionFind(n)
        for v1,v2 in edges:
            if uf.union(v1,v2):
                return [v1,v2]
        