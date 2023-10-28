class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        ans = max(nums)
        
        for i, num in enumerate(nums):
            
            while q and i - q[0][1] > k:
                q.popleft()
            
            val = 0 if not q else q[0][0]
            
            new_num = max(num, num + val)
            ans = max(ans, new_num)
            
            while q and q[-1][0] <= new_num:
                q.pop()
                
            q.append((new_num, i))
        
        return ans