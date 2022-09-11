class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        arr = sorted([(speed[i], efficiency[i]) for i in range(len(speed))], key = lambda x: x[1], reverse=True)
        
        heap = []
        ans = arr[0][0]*arr[0][1]
        tot = cur = 0
        
        # print(arr)
        for sp, ef in arr:
            if len(heap) == k:
                ans = max(ans, tot*cur)
                if sp <= heap[0]:
                    continue
                tot -= heapq.heappop(heap)
            tot += sp
            cur = ef
            heapq.heappush(heap, sp)
            ans = max(ans, tot*cur)
            
        return ans%mod
        
        