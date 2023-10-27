class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        p_sum = [0]
        for num in nums:
            p_sum.append(num + p_sum[-1])
            
        ans = float('inf')
        q = deque()
        for i in range(len(nums) + 1):
            
            while q and p_sum[i] <= p_sum[q[-1]]:
                q.pop()
                
            while q and p_sum[i] - p_sum[q[0]] >= k:
                ans = min(ans, i - q.popleft())
                
            q.append(i)
                
        return ans if ans < float('inf') else -1