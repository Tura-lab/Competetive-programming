class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = [[] for _ in range(len(parent))]
        root = 0
        
        for i in range(len(parent)):
            if parent[i] == -1:continue
            tree[parent[i]].append(i)
            
            
        self.ans = 0
        def dfs(node, p):
            a = b = 0
            for v in tree[node]:
                cur = dfs(v, node)
                if cur > a:
                    b = a
                    a = cur
                elif cur > b:
                    b  = cur
                
            self.ans = max(self.ans, 1+a+b)
            
            if p!=None and s[node] != s[p]:
                return 1 + max(a,b)
            return 0
            
        dfs(root, None)
        return self.ans    
            
            
            