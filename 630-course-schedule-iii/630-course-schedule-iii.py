class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: (x[1], x[0]))
        heap = []
        
        time = 0
        
        for start,end in courses:
            time+=start
            heapq.heappush(heap, -start)
            while time > end:
                time += heapq.heappop(heap)
                    
        return len(heap)