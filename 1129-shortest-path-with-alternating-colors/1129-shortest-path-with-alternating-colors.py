class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1]*n
        
        red = [[]for _ in range(n)]
        blue = [[]for _ in range(n)]
        
        for a,b in redEdges:
            red[a].append(b)
        for a,b in blueEdges:
            blue[a].append(b)
        
        steps = 0
        # print(red)
        # print(blue)
        visited = set([(0, -1)])
        q = deque([(0,-1)])
        while q:
            for _ in range(len(q)):
                node,color = q.popleft()
                if ans[node] == -1:
                    ans[node] = steps
                
                if color == -1 or color == 1:
                    for v in red[node]:
                        if (v,0) not in visited:
                            q.append((v, 0))
                            visited.add((v,0))
                
                if color == -1 or color == 0:
                    for v in blue[node]:
                        if (v,1) not in visited:
                            q.append((v,1))
                            visited.add((v,1))
                
            steps += 1
                        
        return ans