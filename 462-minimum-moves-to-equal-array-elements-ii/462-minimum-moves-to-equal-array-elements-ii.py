class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans_num = nums[len(nums)//2] if len(nums)%2==1 else nums[len(nums)//2-1]
        
        
        ans = 0
        # print(ans_num)
        for num in nums:
            ans += abs(ans_num - num)
            
        return ans