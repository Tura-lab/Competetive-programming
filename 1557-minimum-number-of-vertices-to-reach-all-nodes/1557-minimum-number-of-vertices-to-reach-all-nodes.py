class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        for a,b in edges: ans.discard(b)
        return ans
        
#         graph = [[] for _ in range(n)]
        
#         visited = set()
#         ans = set()
#         for a, b in edges:
#             graph[a].append(b)
            
#         def dfs(node):
#             if node in visited:
#                 return 
#             visited.add(node)
#             ans.add(i)
            
#             for v in graph[node]:
#                 if v in ans:
#                     ans.remove(v)
#                 dfs(v)
            
            
#         for i in range(n):
#             dfs(i)
            
#         return ans