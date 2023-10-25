class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot and do two bin searches
        left_most = nums[0]
        l, r = 0, len(nums) - 1
        pivot = len(nums)
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] < left_most:
                pivot = mid
                r = mid - 1
            else:
                l = mid + 1
            
        def search(left, right):
            l, r = left, right
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return -1
        
        # print(pivot)
        
        ans = search(0, pivot - 1)
        return ans if ans != -1 else search(pivot, len(nums) - 1)