class Solution:
    '''
    3:0,
    3 1 4 1 5
    14,20,24,
    '''
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = set()
        found = set()
        for i in range(len(nums)):
            if nums[i]+k in found:
                ans.add(nums[i]+ nums[i]+k)

            if nums[i]-k in found:
                ans.add(nums[i]+ nums[i]-k)
            found.add(nums[i])
        
        return len(ans)