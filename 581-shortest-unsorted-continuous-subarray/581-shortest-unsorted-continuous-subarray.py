class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        i=0
        j=len(nums)-1
        
        start=end=None
        
        while i<len(nums):
            if nums[i] != s[i]:
                start = i
                break
            i+=1
            
        if start==None:
            return 0
        
        while j>-1: 
            if nums[j] != s[j]:
                return j-start+1
            
            j-=1
            