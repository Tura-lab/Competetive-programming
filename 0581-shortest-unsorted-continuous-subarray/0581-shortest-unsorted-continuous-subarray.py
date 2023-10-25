class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        minStack = [2,]
        
        '''
        minStack = []
        maxStack = []
        
        for i in range(len(nums)):
            while minStack and minStack[-1] > nums[i]:
                minStack.pop()
            
            minStack.append(nums[i])
            
        for i in range(len(nums) - 1, -1, -1):
            while maxStack and maxStack[-1] < nums[i]:
                maxStack.pop()
                
            maxStack.append(nums[i])
            
        
        ans = len(nums)
        i = 0
        while i < len(nums) and i < len(minStack) and minStack[i] == nums[i]:
            i += 1
            ans -= 1
        
        i = 0
        while i < len(nums) and i < len(maxStack) and maxStack[i] == nums[len(nums) - i - 1]:
            i += 1
            ans -= 1
        
        
        return max(ans, 0)