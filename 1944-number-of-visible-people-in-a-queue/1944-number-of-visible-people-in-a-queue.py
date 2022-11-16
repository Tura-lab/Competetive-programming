class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        '''
        3, 1, 2, 1, 1, 0
        '''
        stack = []
        for i in range(n-1, -1, -1):
            count = 0
            while stack and stack[-1] < nums[i]:
                stack.pop()
                count += 1
            
            ans[i] = count + (len(stack) > 0)
            stack.append(nums[i])
            
        return ans