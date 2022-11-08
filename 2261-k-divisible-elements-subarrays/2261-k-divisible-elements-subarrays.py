class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        count = set()
        found = 0
        
        i = 0
        for j in range(len(nums)):
            found += nums[j] % p == 0
            while found > k:
                found -= nums[i] % p == 0
                i += 1
            
            cur = []
            for l in range(j, i-1, -1):
                cur.append(nums[l])
                count.add(tuple(cur))
            
        return len(count)