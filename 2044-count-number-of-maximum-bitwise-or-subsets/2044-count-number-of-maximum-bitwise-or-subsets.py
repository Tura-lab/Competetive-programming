class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans|=num
            
        self.tot = 0
        self.seen = set()
        def dfs(i, yet):
            if i==len(nums):
                if yet == ans:
                    self.tot+=1
                return 

            dfs(i+1, yet)
            dfs(i+1, yet|nums[i])
        
        dfs(0,0)
        
        return self.tot