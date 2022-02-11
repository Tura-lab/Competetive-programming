class Solution:
    '''
    1,-1,3,4
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] < len(nums)+1 and i != nums[i]-1 and nums[nums[i]-1] != nums[i]:
                val = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i]=val   
            i+=1
        
        for i in range(1, len(nums)+1):
            if nums[i-1] != i:
                return i
        return i+1
                
        
#         seen = set()
#         missing = 1
        
#         for num in nums:
#             if num == missing:
#                 missing+=1
#                 while missing in seen:
#                     missing+=1
#             seen.add(num)
                
#         return missing

        
        
        
        
        
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] >= 0:
#                 break
                
#         missing = 1
#         for j in range(i, len(nums)):
#             if nums[j]>missing:
#                 return missing
#             if nums[j] == missing:
#                 missing = nums[j]+1
        
#         return missing
        