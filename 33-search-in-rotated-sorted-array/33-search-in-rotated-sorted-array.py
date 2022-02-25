class Solution:
    '''
    4, 5 ,6, 7, 0, 1, 2
    '''
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r = len(nums)-1
        num = nums[0]
        
        while l<=r:
            mid = (l+r)//2
            # print(l,r,mid)
            if nums[mid] < num and (mid-1<0 or nums[mid-1]>=num):
                break
            if nums[mid] >= num:
                l = mid+1
            else:
                r = mid-1
        # print(l,r,mid)
        start = 0
        end = mid-1 if mid!=0 else len(nums)-1
        while start<=end:
            m = (start+end)//2

            if nums[m] == target:
                return m
            elif nums[m]<target:
                start=m+1
            else:
                end=m-1
        
        if mid==0:
            return -1
    
        start = mid
        end = len(nums)-1
        while start<=end:
            m = (start+end)//2

            if nums[m] == target:
                return m
            elif nums[m]<target:
                start=m+1
            else:
                end=m-1
        return -1