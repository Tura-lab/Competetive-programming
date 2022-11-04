class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        found = defaultdict(int)
        found[0] += 1
        cur = 0
        
        
        ans = 0
        for num in nums:
            cur += num
            val = cur % k
            ans += found[val]
            found[val] += 1
            
            
        return ans