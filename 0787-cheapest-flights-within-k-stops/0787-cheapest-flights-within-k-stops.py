class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, c in flights:
            graph[a].append((b, c))
        
        @cache
        def dfs(stops, node):
            if stops - 1 > k:
                return float('inf')
            if node == dst:
                return 0
            
            ans = float('inf')
            for v, w in graph[node]:
                ans = min(ans, w + dfs(stops + 1, v))
                
            return ans
        
        ans = dfs(0, src)
        
        return ans  if ans !=float('inf') else -1