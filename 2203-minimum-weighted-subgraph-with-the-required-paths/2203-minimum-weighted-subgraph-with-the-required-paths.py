class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        toDest = [float('inf') for _ in range(n)]
        fromA = [float('inf') for _ in range(n)]
        fromB = [float('inf') for _ in range(n)]
        
        graph = [[] for _ in range(n)]
        reversed_graph = [[] for _ in range(n)]
        for a, b, c in edges:
            graph[a].append((b, c))
            reversed_graph[b].append((a, c))
            
        def d2(start, graph):
            distances = [float('inf') for _ in range(n)]
            heap = []
            heappush(heap, (0, start))
            while heap:
                cost, node = heappop(heap)
                if distances[node] == float('inf'):
                    distances[node] = cost

                    for v, w in graph[node]:
                        if distances[v] == float('inf'):
                            heappush(heap, (cost + w, v))
            
            return distances

        
        from1 = d2(src1, graph)
        from2 = d2(src2, graph)
        toDest = d2(dest, reversed_graph)
        
        ans = float('inf')
        for mid in range(n):
            ans = min(ans, from1[mid] + from2[mid] + toDest[mid])
        
        return ans if ans < float('inf') else -1
    
    
    
    
    