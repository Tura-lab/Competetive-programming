class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        Input: nums = [1,1,4,2,3], x = 5
        
        0,1,2,6,8,11
        '''
        p_sum = [0]
        for num in nums:
            p_sum.append(num + p_sum[-1])
        
        ans = len(nums) + 1
        
        right_sum = 0
        
        for right in range(len(p_sum)-1, -1, -1):
            
            l, r = 0, right
            while l <= r:
                mid = l + (r-l)//2
                
                if right_sum + p_sum[mid] == x:
                    ans = min(ans, mid + len(p_sum)-right-1 )
                    break
                    
                if right_sum + p_sum[mid] < x:
                    l = mid+1
                else:
                    r = mid-1
            
            right_sum += nums[right-1]
        
        if ans == len(nums) + 1:
            return -1
        return ans