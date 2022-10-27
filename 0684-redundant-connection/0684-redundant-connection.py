class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1] * (n+1)
        
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            
            if pu == pv:
                return False
            
            if size[pu] > size[pv]:
                parent[pv] = pu
            else:
                parent[pu] = pv
            
            return True
        
        ans = None
        for u,v in edges:
            if not union(u,v):
                ans = [u,v]
        return ans