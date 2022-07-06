class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(nums)
        count = nums.count(0)

        i = n-1
        while i>-1:
            if nums[i] == 0:
                count -= 1
            if i + count<n:
                nums[i + count] = nums[i]
                if nums[i + count] == 0 and i + count + 1 < n:
                    nums[i + count + 1] = 0
            
            i-=1
            
        # print(shifts)
        # print(nums)
        