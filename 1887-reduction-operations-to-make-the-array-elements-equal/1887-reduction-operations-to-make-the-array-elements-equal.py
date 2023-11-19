class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        '''
        5, 3, 1
        '''
        counts = Counter(nums)
        nums = list(set(nums))
        n = len(nums)
        nums.sort(reverse = True)
        
        ans,count = 0, 0
        for i in range(len(nums)):
            if i < n - 1:
                count += counts[nums[i]]
                ans += count
                
        return ans