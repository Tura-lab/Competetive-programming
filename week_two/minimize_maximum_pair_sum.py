def minPairSum(self, nums: List[int]) -> int:
    nums.sort()
    # return nums[0]+nums[-1]
    arr = []
    i=0
    j=-1
    while i<len(nums)//2:
        if nums[i] + nums[j] not in arr:
            arr.append(nums[i] + nums[j])
        i+=1
        j-=1
    return max(arr)
