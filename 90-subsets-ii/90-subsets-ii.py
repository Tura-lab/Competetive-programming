class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        def helper(nums, i, ans):
            if i==len(nums):
                return final.append(ans) if ans not in final else None
            helper(nums, i+1, ans+[nums[i]])
            helper(nums, i+1, ans)
        
        nums.sort()
        helper(nums, 0, [])
        return final