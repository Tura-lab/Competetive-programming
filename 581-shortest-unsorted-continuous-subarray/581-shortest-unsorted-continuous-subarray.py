class Solution:
    '''
    2,6,4,8,10,9,15
        i
               j
    2,4,
    15,10,8,6,2 
    s = 1
    '''
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i=0        
        start = None
        stack = []
        while i<len(nums):
            while stack and stack[-1]>nums[i]:
                stack.pop()
                start = len(stack) if start==None else min(len(stack), start)
            
            stack.append(nums[i])
            i+=1
        
        i = len(nums)-1
        end = None
        stack = []
        while i>-1:
            while stack and stack[-1]<nums[i]:
                stack.pop()
                end = len(stack) if end==None else min(len(stack), end)
            
            stack.append(nums[i])
            i-=1
        
        if end==None or start==None:
            return 0
        end = len(nums)-end-1
        
        return end-start+1