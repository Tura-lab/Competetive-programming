class Solution:
    '''
    [0]
    -4, -1, 0, 3, 10
         i   
               j 
    '''
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [0]*len(nums)
        i=0
        j=k=len(nums)-1
        while k>-1:
            if abs(nums[i]) > abs(nums[j]):
                new[k]=nums[i]**2
                i+=1
            else:
                new[k]=nums[j]**2
                j-=1
            k-=1
        
        return new
        
        
        
        
        
#         new = []
#         if nums[0]>=0:
#             for i in range(len(nums)):
#                 nums[i] = nums[i]**2
#             return nums
        
#         if nums[-1]<0:
#             for i in range(len(nums)-1, -1, -1):
#                 new.append(nums[i]**2)
#             return new
#         for j in range(len(nums)):
#             if nums[j]>=0:
#                 break
#         i=j-1
        
#         while i>-1 and j<len(nums):
#             if -1*nums[i] < nums[j]:
#                 new.append(nums[i]**2)
#                 i-=1
#             else:
#                 new.append(nums[j]**2)
#                 j+=1
#         while i>-1:
#             new.append(nums[i]**2)
#             i-=1
#         while j<len(nums):
#             new.append(nums[j]**2)
#             j+=1
#         return new
        