class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        dp = [[0] * 26 for _ in range(n)]
        
        graph = [[] for _ in range(n)]
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node, label in enumerate(labels):
            dp[node][ord(label) - ord('a')] += 1
        
        def dfs(node, parent):
            for v in graph[node]:
                if v == parent:continue
                    
                dfs(v, node)
                
                for i in range(26):
                    dp[node][i] += dp[v][i]
        
        dfs(0, -1)
        
        ans = []
        for node in range(n):
            ans.append(dp[node][ord(labels[node]) - ord('a')])
            
        return ans
            