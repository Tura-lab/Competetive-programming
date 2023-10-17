class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
        {1, 1*2*2, 1*3*3, 1*4*4}
        {2, 2*2*2, 2*3*3, 2*4*4}
        {3, 2*2*3, 3*3*3, 3*4*4}
        {4, 4*2*2, 4*3*3, 4*4*4}
        {5, 5*2*2, 5*3*3, 5*4*4}
        {6, 6*2*3, 6*3*3, 6*4*4}
        '''
        
        ans = 0
        for i in range(1, 10000):
            cur_sum = 0
            idx = i
            cur_num = 1
            while idx <= len(nums):
                cur_sum += nums[idx-1]
                cur_num += 1
                idx = i * cur_num * cur_num
                
            ans = max(ans, cur_sum)
            
        return ans