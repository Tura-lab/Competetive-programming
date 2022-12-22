class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.ans = 0
        
        counts = [1] * n
        sum_of_distance = [0] * n
        
        tree = [[] for _ in range(n)]
        
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def dfs(node, parent):
            
            for v in tree[node]:
                if v == parent:continue
                child_count = dfs(v, node)
                sum_of_distance[node] += sum_of_distance[v] + counts[v]
                counts[node] += counts[v]
                
        dfs(0, -1)
        
        def dfs(node, parent):
            for v in tree[node]:
                if v == parent:continue
                sum_of_distance[v] += (sum_of_distance[node] + n - counts[v]) - (sum_of_distance[v] + counts[v])                
                dfs(v, node)
                
        
        dfs(0, -1)
                
        return sum_of_distance