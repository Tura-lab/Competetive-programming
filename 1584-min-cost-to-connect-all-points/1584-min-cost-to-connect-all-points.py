class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i,len(points)):
                x2, y2 = points[j]
                graph[(x1,y1)].append((abs(x1-x2)+abs(y1-y2), (x2,y2)))
                if i!=j:
                    graph[(x2,y2)].append(( abs(x1-x2)+abs(y1-y2), (x1,y1)))
        
        heap = []
        heapq.heappush(heap, (0,points[0]))
        ans = 0
        while heap and len(visited)<len(points):
            cost, (x,y)= heapq.heappop(heap)
            if (x,y) in visited:
                continue
            ans+=cost
            visited.add((x,y))
            
            for point in graph[(x,y)]:
                cost, (x1,y1) = point
                if (x1,y1) not in visited:
                    heapq.heappush(heap, point)
        
        return ans 