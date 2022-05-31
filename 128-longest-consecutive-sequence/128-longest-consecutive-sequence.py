class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        found = {}
        
        ans = 0
        for num in nums:
            if num in found:
                continue
                
            found[num] = 0
            if num-1 in found:
                found[num] += found[num-1]
            if num+1 in found:
                found[num] += found[num+1]
            
            found[num]+=1
            if num-1 in found:
                found[num-1-found[num-1]+1] = found[num]
            if num+1 in found:
                found[num+1+found[num+1]-1] = found[num]
                
            ans = max(ans, found[num])
                
        # print(found)
        # print(sorted(nums))
        return ans