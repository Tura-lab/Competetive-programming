class Solution:
    '''
    1, 3, 4, 2, 2
    1 2 3 4
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        def count(arr,start,end):
            count = 0
            for num in nums:
                if start<=num<=end:
                    
                    count+=1
            return count
        
        l = 1
        r = max(nums)+1
        
        while l<=r:
            mid = (l+r)//2
            # print(l,r,mid)
            if count(nums, l, mid) > mid-l+1:
                r=mid-1
            else:
                l=mid+1
                
            
        return l