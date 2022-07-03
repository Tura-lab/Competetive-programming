class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        found = False
        i = 1
        while i<len(nums) and nums[i] == nums[0]: i+=1

        if i<len(nums) and nums[i] > nums[0]: found = True
        
        num = 1 if len(nums)>1 and found else -1
        
        count = 1
        past = nums[0]
        for i in range(i, len(nums)):
            if (nums[i] - past)*num > 0:
                count += 1
                num   *= -1
            past = max(past, nums[i]) if num==-1 else min(past, nums[i])
                
        return count
                
        