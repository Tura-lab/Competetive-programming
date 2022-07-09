from heapq import heappush, heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # print(n)
        # dp = [-1]*n
        
        pos = []

        for i in range(n-1, -1, -1):

            while pos and pos[0][1] > i+k:
                heapq.heappop(pos)

            ans = -nums[i] if not pos else pos[0][0] - nums[i]
            heapq.heappush(pos, (ans, i))
            
        # print(pos)
        return -ans

    
    



    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         @cache
#         def solve(i):
#             if i==n-1:
#                 return nums[i]
            
#             ans = -float('inf')
#             for j in range(i+1, min(i+k+1, n)):
#                 ans = max(ans, nums[i] + solve(j))

#             return ans
            
#         return solve(0)