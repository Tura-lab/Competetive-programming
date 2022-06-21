class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """                
        found = False
        for i in range(len(nums)-1, -1, -1):
            mn = None
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    if not mn:
                        mn = j
                        continue
                    if nums[j] < nums[mn]:
                        mn = j
            if mn:
                found = True
                nums[i], nums[mn] = nums[mn], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                break
                
        
        if not found:
            nums.sort()
                
        
        