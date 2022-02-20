class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if target<=nums[0] else len(nums)
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        
        def bs(arr, start, end,val):
            mid = (start+end)//2
            if arr[mid] == target:
                return mid
            if arr[mid]>target and arr[mid-1]<target:
                return mid
            if arr[mid]<target and arr[mid+1]>target:
                return mid+1

            if arr[mid] < val:
                return bs(arr, mid, end,val)
            else:
                return bs(arr,start,mid,val)
            
        return bs(nums, 0, len(nums), target)