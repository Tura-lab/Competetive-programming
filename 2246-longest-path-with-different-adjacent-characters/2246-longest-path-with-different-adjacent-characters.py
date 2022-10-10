class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = [[] for _ in range(len(parent))]
        root = 0
        
        for i in range(len(parent)):
            if parent[i] == -1:continue
                
            tree[parent[i]].append(i)
            
            
        self.ans = 0
        def dfs(node, p):
            
            heap = []
            for v in tree[node]:
                heapq.heappush(heap, -dfs(v,node))
              
            if len(heap)==0:
                a = 0
                b = 0
            elif len(heap) == 1:
                a = -heappop(heap)
                b = 0
            else:
                a = -heappop(heap)
                b = -heappop(heap)
                
            self.ans = max(self.ans, 1+a+b)
            
            if p!=None and s[node] != s[p]:
                # print(node, p, (left,right))
                return 1 + max(a,b)
            return 0
            
        dfs(root, None)
        return self.ans    
            
            
            