# from functools import lru_cache

class Solution:
    '''
    10,9,2,5,3,7,101,18
    2 3 7 101 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        _max = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    _max = max(dp[i], _max)
                    
        return _max
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #Binary search to find the correct index of replacement
#         def findPosAndReplace(num,s, e):
#             mid = (s+e)//2
#             if arr[mid] >= num and (mid-1<0 or arr[mid-1] < num):
#                 arr[mid] = num
#                 return
#             if arr[mid] > num:
#                 findPosAndReplace(num,s,mid)
#             else:
#                 findPosAndReplace(num,mid,e)
        
#         arr = []
#         for num in nums:
#             if arr==[] or num>arr[-1]:
#                 arr.append(num)
#             else:
#                 findPosAndReplace(num,0,len(arr))
#         return len(arr)
    
#     # DP (TLE)
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
        
#         cache = [-1]*(len(nums)+1)
#         def helper(end, i):
#             if i >= len(nums):
#                 return 0
#             if cache[end+1] !=-1:
#                 return cache[end+1]
#             dont = helper(end, i+1)
#             pick = 0
#             if end==-1 or nums[i]>nums[end]:
#                 pick = 1+helper(i, i+1)
#             cache[end+1] = max(pick, dont)
#             return cache[end+1]
#         # print(cache)
#         return helper(-1,0)