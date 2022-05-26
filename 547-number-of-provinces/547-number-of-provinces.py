class UnionFind:
    def __init__(self, n):
        self.reps = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, v):
        if v == self.reps[v]:
            return v
        return self.find(self.reps[v])
    
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        
        if p1==p2:
            return
        
        r1 = self.rank[p1]
        r2 = self.rank[p2]
        
        if r1 == r2 or r1>r2:
            self.rank[r1] +=r2
            self.reps[p2] = p1
        else:
            self.rank[r2] +=r1
            self.reps[p1] = p2

            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        components = UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    components.union(i,j)
        
        count =0 
        for i in range(n):
            if components.reps[i] == i:
                count+=1

        return count
        
        
    