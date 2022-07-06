class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(nums)
        shifts = [0]*n
        count = 0
        
        for i in range(n):
            shifts[i] = count
            if nums[i] == 0:
                count +=1
            
            
        i = n-1
        while i>-1:
            if i + shifts[i]<n:
                # print(i + shifts[i], i)
                nums[i + shifts[i]] = nums[i]
                if nums[i + shifts[i]] == 0 and i + shifts[i] + 1 < n:
                    nums[i + shifts[i] + 1] = 0

            i-=1
            
        # print(shifts)
        # print(nums)
        