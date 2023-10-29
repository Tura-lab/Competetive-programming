class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        found = {}
        ans = 0 
        
        cur = 0
        for i, num in enumerate(nums):
            if num == 0:
                cur -= 1
            else:
                cur += 1
                
            if cur in found or cur == 0:
                ans = max(ans, i - found[cur] if cur != 0 else i + 1)
                
            else:
                found[cur] = i
                
        return ans