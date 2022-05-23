class Solution:
    def minimumTime(self, n: int, r: List[List[int]], time: List[int]) -> int:
        indeg = {i:0 for i in range(1, n+1)}
        graph = {i:[] for i in range(1, n+1)}
        start_time = {i:0 for i in range(1, n+1)}
        
        for prev,cur in r:
            graph[prev].append(cur)
            indeg[cur]+=1
            
        q = collections.deque()
        
        for course in graph.keys():
            if indeg[course] == 0:
                q.append(course)
                
        while q:
            course = q.popleft()
            for v in graph[course]:
                indeg[v]-=1
                if indeg[v] == 0:
                    q.append(v)
                start_time[v] = max(start_time[v], start_time[course] + time[course-1])
            
        _max = 0
        for course in start_time.keys():
            _max = max(_max, start_time[course] + time[course-1])
            
        # print(start_time)
        return _max