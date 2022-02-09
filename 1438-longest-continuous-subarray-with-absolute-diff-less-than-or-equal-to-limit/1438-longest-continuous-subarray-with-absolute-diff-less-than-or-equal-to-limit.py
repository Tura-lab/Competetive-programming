from collections import deque

class Solution:
    '''
    max = [7]
    min = [2,4,7] 
    8 2 4 7  ,4
      i
          j
    
    '''
    def longestSubarray(self, nums, limit):
        max_d = deque()
        min_d = deque()
        i=j=0
        while j<len(nums):
            while max_d and max_d[-1]<nums[j]:
                max_d.pop()
            max_d.append(nums[j])
            while min_d and min_d[-1]>nums[j]:
                min_d.pop()
            min_d.append(nums[j])
            
            if max_d[0]-min_d[0] > limit:
                if max_d[0] == nums[i]:
                    max_d.popleft()
                if min_d[0] == nums[i]:
                    min_d.popleft()
                i+=1
            j+=1
        # print(max_d)
        # print(min_d)
        return j-i
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums)==1:
        #     return 1
        # i=0
        # j=1
        # ans = 0
        # mx = max(nums[i:j+1])
        # mn = min(nums[i:j+1])
        # while j<len(nums):
        #     if mx-mn <= limit:
        #         ans = j-i+1
        #         j+=1
        #         if j==len(nums):
        #             break
        #         if nums[j]<mn:
        #             mn = nums[j]
        #         elif nums[j]>mx:
        #             mx = nums[j]
        #     else:
        #         i+=1
        #         j+=1
        #         if j==len(nums):
        #             break
        #         if nums[i-1]==mn:
        #             mn = min(nums[i:j+1])
        #         elif nums[i-1]==mx:
        #             mx = max(nums[i:j+1])
        #         if nums[j]<mn:
        #             mn = nums[j]
        #         elif nums[j]>mx:
        #             mx = nums[j]
        # return ans