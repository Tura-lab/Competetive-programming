class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        
        def dfs(node):
            nonlocal ans
            if node == n-1:
                ans.append(path[:])
                return
            for v in graph[node]:
                path.append(v)
                dfs(v)
                path.pop()

        path = [0]
        dfs(0)
        return ans