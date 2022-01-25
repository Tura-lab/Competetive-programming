class Solution:
    '''
    zeros=2
    1 1 1 0 0 0 1 1 1 1 0 , k=2, ans=6
            i
                        j
    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=j=zeros=0
        for j in range(len(nums)):
            if zeros > k:
                if nums[i] ==0:
                    zeros-=1
                i+=1
            if nums[j]==0:
                zeros+=1         
    
        return j-i+1 if zeros<=k else j-i 
        