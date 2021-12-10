def selection_sort(self, nums):
    for j in range(len(nums)):
        smallest = j
        for i in range(j, len(nums)):
            if nums[i] <= nums[smallest]:
                smallest = i
        nums[smallest], nums[j] = nums[j], nums[smallest]

    return nums
def targetIndices(self, nums, target):
    nums = self.selection_sort(nums)
    ar = []
    for i in range(len(nums)):
        if nums[i]==target:
            ar.append(i) 
    return ar
