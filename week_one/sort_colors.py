def sortColors(self, nums: List[int]) -> None:
    for j in range(len(nums)):
        smallest = j
        for i in range(j, len(nums)):
            if nums[i] <= nums[smallest]:
                smallest = i
        nums[smallest], nums[j] = nums[j], nums[smallest]      
