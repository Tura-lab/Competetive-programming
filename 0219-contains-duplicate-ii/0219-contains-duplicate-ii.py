class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = Counter()
        
        i = 0
        for j in range(len(nums)):
            counts[nums[j]] += 1
            
            if j - i > k:
                counts[nums[i]] -= 1
                if counts[nums[i]] == 0:
                    del counts[nums[i]]
                    
                i += 1
            
            if len ( counts) < j - i + 1:
                return True
            
        return False