class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 3 2 0
            i
            j
        """
        i=0
        for j in range(len(nums)):
            if nums[i]==0 and nums[j]!=0:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
            elif nums[i]!=0:
                i+=1
