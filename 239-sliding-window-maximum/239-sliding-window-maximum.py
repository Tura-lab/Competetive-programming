from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i in range(len(nums)):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
            if i - q[0][1] >= k:
                q.popleft()
            
            if i+1>=k:
                ans.append(q[0][0])
            
        return ans