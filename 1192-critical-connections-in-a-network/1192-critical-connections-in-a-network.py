class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
            
        index_of = [-1 for i in range(n)]
        lowest_from = [-1 for i in range(n)]
        
        bridges = []
        seen = set()
        def dfs(node, i, parent):
            index_of[node] = i
            lowest_from[node] = i
            
            for v in graph[node]:
                if lowest_from[v]!=-1 and v!= parent:
                    lowest_from[node] = min(lowest_from[node], lowest_from[v])
                if v not in seen and v!=parent:
                    seen.add(v)
                    index = dfs(v, i+1, node)
                    
                    if i < index:
                        bridges.append([node, v])
                    
                    lowest_from[node] = min(lowest_from[node], index)
                    
            return lowest_from[node]
        
        seen.add(0)
        dfs(0,1,None)
        return bridges