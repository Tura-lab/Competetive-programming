class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(len(nums)-1, i, -1):
                if j<len(nums)-1 and nums[j+1] == nums[j]:
                    continue
                k = i+1
                l = j-1
                num = target-nums[i]-nums[j]
                
                while k<l:
                    cur = nums[k] + nums[l]
                    if cur > num:
                        l-=1
                    elif cur < num:
                        k+=1
                    else:
                        val = nums[l]
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while k<l and nums[l] == val:
                            l-=1
                        
                        val = nums[k]
                        while k<l and nums[k] == val:
                            k+=1

        return ans
                            
                        
                
                            
                            