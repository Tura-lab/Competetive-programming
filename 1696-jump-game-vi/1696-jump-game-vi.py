'''
  1 -1 -2  4  -7  3
  0  6    
  
'''
from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums)<3:
            return sum(nums)
        ans = deque()
        
        ans.appendleft(len(nums)-1)
        val = nums[-2]+nums[-1]
        nums[-2]= val
        
        while ans and nums[ans[0]] < val:
            ans.popleft()
        ans.appendleft(len(nums)-2)
        
        i=len(nums)-3
        while i>-1:
            while ans[-1]-i>k:
                ans.pop()
                
            val = nums[ans[-1]] + nums[i]
            nums[i] = val
            
            while ans and nums[ans[0]]<val:
                ans.popleft()
            ans.appendleft(i)            
            
            i-=1
        return val
        
        
        
        
        
        
        
        
        
        
#         TLE
#         if len(nums)<3:
#             return sum(nums)
        
#         dp = [-(10)**5]*(len(nums)+1)
#         def helper(end, cur): 
#             if dp[end] != -(10)**5:
#                 return dp[end]
#             if cur == len(nums)-1:
#                 return 0
            
#             pick = nums[cur] + helper(cur, cur+1)
#             if cur-end ==k:
#                 dp[end] = pick
#                 return dp[end]
#             dont = helper(end, cur+1)
            
#             dp[end] = max(pick, dont)
            
#             return dp[end]
#         print(len(nums))
#         return helper(0,1) + nums[0] + nums[-1]