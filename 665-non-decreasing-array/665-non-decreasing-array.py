class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                if i-2 <0 or nums[i-2]<=nums[i]:
                    nums[i-1] = nums[i]
                    count+=1
                else:
                    nums[i] = nums[i-1]
                    count+=1
                    
        return count<2