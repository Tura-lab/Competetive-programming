class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tot = 0
        for num in nums:
            if not num&1:
                tot += num
        ans = []
        
        for val, i in queries:
            num = val + nums[i] 
            if not num&1:
                if not nums[i]&1:
                    tot -= nums[i]
                tot += num
            else:
                if not nums[i]&1:
                    tot -= nums[i]
            
            nums[i] = num
            ans.append(tot)
            
        return ans
        
                