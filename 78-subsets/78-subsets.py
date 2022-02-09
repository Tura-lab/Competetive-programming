class Solution:
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        def helper(nums, i, ans):
            if i==len(nums):
                return final.append(ans)
                
            helper(nums, i+1, ans) #Exclude
            helper(nums, i+1, ans + [nums[i]]) #Include
            
        helper(nums, 0, [])
        return final