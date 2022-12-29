class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:        
        tasks = sorted([(tasks[i], i) for i in range(len(tasks))], key = lambda x: x[0][0])
        print(tasks)
        
        cur_time = 0
        heap = []
        idx = 0
        answer = []
        
        
        while len(answer) < len(tasks):
            while idx < len(tasks) and cur_time >= tasks[idx][0][0]:
                heappush(heap, (tasks[idx][0][1], tasks[idx][1]))                
                idx += 1
                
            if heap:
                val = heappop(heap)
                answer.append(val[1])
                cur_time += val[0]
            else:
                if idx < len(tasks):
                    cur_time = tasks[idx][0][0]
            
        return answer