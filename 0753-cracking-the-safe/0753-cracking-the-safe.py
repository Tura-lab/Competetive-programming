class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        cur = "0" * (n - 1)
        
        ans = []
        visited = set()
        
        def dfs(node):
            for i in range(k):
                # so i is the edge that connects the two nodes
                cur_node = node + str(i)
                
                if cur_node not in visited:
                    visited.add(cur_node)
                    dfs(cur_node[1:])
                    ans.append(str(i))
                    
        dfs(cur)
                    
        return "".join(ans) + cur