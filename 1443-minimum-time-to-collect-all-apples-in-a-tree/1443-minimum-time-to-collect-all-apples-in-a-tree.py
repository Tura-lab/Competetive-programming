class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        subtree_has_apples = [False] * n
        
        def dfs(node, parent):
            for v in graph[node]:
                if v == parent:
                    continue
                if dfs(v, node):
                    subtree_has_apples[node] = True
                    
            return subtree_has_apples[node] or hasApple[node]
        
        dfs(0, -1)
        
        # print(subtree_has_apples)
        
        def dfs(node, parent):
            if not subtree_has_apples[node]:
                return 0 + hasApple[node]
            
            count = 0
            for v in graph[node]:
                if v == parent:continue
                    
                child = dfs(v, node)
                count += child + (child != 0)
            
            count += node != 0
            
            return count
            
        ans = dfs(0, -1)
        
        return 0 if ans == 1 else ans
