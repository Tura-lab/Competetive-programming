class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        j=0
        for i in range(1,len(nums)):
            while j<i and nums[i]-nums[j] > 1:
                j+=1
            
            if j<i and nums[i]-nums[j]==1:  
                # print(j, i)
                ans = max(ans, i-j+1)
                
        return ans