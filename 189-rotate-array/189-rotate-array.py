class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        5 6 7 4 1 2 3,     k=3
        """
        #O(1) space
        k = k%len(nums)
        if k>0:
            nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
        return
        #O(n) space
        new = []
        k = len(nums)-k
        while k<len(nums):
            new.append(nums[k])
            k+=1
        i=0
        while len(new)<len(nums):
            new.append(nums[i])
            i+=1
        for i in range(len(new)):
            nums[i] = new[i]