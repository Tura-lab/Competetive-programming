class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        ans = 456345634563456
        
        final = 1
        for i in range(1, len(graph)):
            final |= 1<<i
        
        # print(final)
        def findPath(i, final):
            q = collections.deque()
            seen = set()
            path = 1<<i
            q.append((path, i))
            seen.add((path, i))
            
            dist=1
            while q:
                # print(q)
                for _ in range(len(q)):
                    path, cur = q.popleft()
                    for v in graph[cur]:
                        num = path | (1<<v)
                        if num == final:
                            return dist
                        if (num, v) not in seen:
                            seen.add((num, v))
                            q.append((num, v))
                        
                dist+=1
            return 0
        for i in range(0, len(graph)):
            # print(num)
            ans = min(findPath(i, final), ans)
            
        return ans
            