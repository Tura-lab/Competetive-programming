class Solution:
    def longestWPI(self, nums: List[int]) -> int:
        '''
        9  9   6  0  6  6  9

        1  1  -1  -1  -1  -1   1
     0  1  2   1   0  -1  -2  -1
        '''
        for i in range(len(nums)):
            nums[i] = 1 if nums[i]>8 else -1
            
        p_sum = [0]
        for num in nums:
            p_sum.append(p_sum[-1]+num)
            
        seen = {}
        ans = float('-inf') 
        for i in range(len(p_sum)):
            if p_sum[i]>0:
                ans = i
                continue
            if p_sum[i]-1 in seen:
                ans = max(ans, i-seen[p_sum[i]-1])
            if p_sum[i] not in seen:
                seen[p_sum[i]] = i
                
        return max(ans,0)