class Solution:
    def longestSubarray(self, nums, limit):
        if len(nums)==1:
            return 1
        i=0
        j=1
        ans = 0
        mx = max(nums[i:j+1])
        mn = min(nums[i:j+1])
        while j<len(nums):
            if mx-mn <= limit:
                ans = j-i+1
                j+=1
                if j==len(nums):
                    break
                if nums[j]<mn:
                    mn = nums[j]
                elif nums[j]>mx:
                    mx = nums[j]
            else:
                i+=1
                j+=1
                if j==len(nums):
                    break
                if nums[i-1]==mn:
                    mn = min(nums[i:j+1])
                elif nums[i-1]==mx:
                    mx = max(nums[i:j+1])
                if nums[j]<mn:
                    mn = nums[j]
                elif nums[j]>mx:
                    mx = nums[j]
        return ans
