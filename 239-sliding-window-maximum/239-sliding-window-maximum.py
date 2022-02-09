from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_d = deque()
        ans = []
        i=0
        j=0
        while j<len(nums):
            while max_d and max_d[-1]<nums[j]:
                max_d.pop()
            max_d.append(nums[j])
            
            j+=1
            if j>=k:
                ans.append(max_d[0])
                if nums[i] == max_d[0]:
                    max_d.popleft()
                i+=1
        return ans