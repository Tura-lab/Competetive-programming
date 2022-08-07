class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        row = col = 10**6
        blocked_set = set(map(tuple, blocked))
        limit = len(blocked)
        
        def isValid(r,c,visited):
            if -1<r<row and -1<c<col and (r,c) not in blocked_set and (r,c) not in visited:
                return True
            return False
        
        # do BFS from both the source and the target
        def bfs(start,end):
            q = collections.deque()
            visited = set()
            q.append((start[0], start[1]))
            
            while q:
                # print(q)
                x,y = q.popleft()
                # print([x,y],end, [x,y]==end)
                if [x,y]==end or abs(x-start[0]) + abs(y-start[1]) > limit:
                    return True
                
                # Up
                if isValid(x, y-1,visited):
                    q.append((x, y-1))
                    visited.add((x,y-1))
                # Down
                if isValid(x, y+1,visited):
                    q.append((x, y+1))
                    visited.add((x,y+1))
                # Right
                if isValid(x+1, y,visited):
                    q.append((x+1, y))
                    visited.add((x+1,y))
                # Left
                if isValid(x-1, y,visited):
                    q.append((x-1, y))
                    visited.add((x-1,y))

            return False
        
        return bfs(source,target) and bfs(target,source)
                