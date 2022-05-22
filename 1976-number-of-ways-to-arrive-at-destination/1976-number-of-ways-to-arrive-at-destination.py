from heapq import heapify, heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        road_graph = [[] for _ in range(n)]
        
        for v1, v2, time in roads:
            road_graph[v1].append((v2,time))
            road_graph[v2].append((v1, time))
        
        
        mod = (10**9) +7
        
        ways = {i:[float('inf'),0] for i in range(n)}
        ways[0] = [0,1]
        
        distances = [(0,0)]
        
        while distances:
            dist, node = heappop(distances)
            if dist > ways[n-1][0]:
                break
                
            for v, d in road_graph[node]:
                if dist+d > ways[v][0]:
                    continue
                elif dist+d == ways[v][0]:
                    ways[v][1] += ways[node][1]
                else:
                    ways[v][0] = dist + d
                    ways[v][1] = ways[node][1]
                    heappush(distances, (dist+d, v))
                
        return ways[n-1][1] % mod