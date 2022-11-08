class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        
        length = 0
        tot = 0
        i = 0
        for j in range(len(nums)):
            length += 1
            tot += nums[j]
            while length * tot >= k:
                length -= 1
                tot -= nums[i]
                i += 1
            
            count += j - i + 1
        
        return count