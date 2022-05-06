class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        instack = set()
        seen = set()
        
        def dfs(node):
            instack.add(node)
            for n in graph[node]:
                if n in instack:
                    return False
                
                if n not in seen:
                    ans = dfs(n)
                    if ans==False:
                        return ans
            
            instack.remove(node)
            seen.add(node)
        
        for i in range(len(graph)):
            if dfs(i) != False:
                ans.append(i)

        return ans