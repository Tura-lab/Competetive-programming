class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
           10   5   2    6
        1  10   50  100  600
        
        
           1   2   3
        1  1   2   6
        
        '''
        # pref = [1]
        # for num in nums:
        #     pref.append(pref[-1]*num)
            
        count = 0
        i=j=0
        
        prod = 1
        while j<len(nums):
            prod*=nums[j]
            while i<=j and prod >= k:
                prod/=nums[i]
                i+=1
                
            count += j-i+1
            j+=1
            
        return count
    
#         pref = [1]
#         for num in nums:
#             pref.append(pref[-1]*num)
            
#         count = 0
#         lowest = 0 
#         for i in range(1, len(pref)):
#             for j in range(lowest, i):
#                 if pref[i]/pref[j] < k:
#                     lowest = j
#                     count+=(i-j)
#                     break
            
#         return count