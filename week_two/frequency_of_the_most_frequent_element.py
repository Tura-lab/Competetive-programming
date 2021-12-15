def maxFrequency(self, nums: List[int], k: int) -> int:
    start=end=maximum=total=0
    nums.sort()
    while end<len(nums):
        total+=nums[end]
        if nums[end]*(end-start+1) <= total+k:
            maximum +=1
        else:
            total-=nums[start]
            start+=1
        end+=1
    return maximum
