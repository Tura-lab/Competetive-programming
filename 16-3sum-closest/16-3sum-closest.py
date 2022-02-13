class Solution:
    '''
    -1,2,1,-4
    -4,-1,1,2
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # print(len(nums))
        nums.sort()
        closest = 10**5
        for i in range(len(nums)):
            t = target - nums[i]
            l=0
            r = len(nums)-1
            
            while l<r:
                if i == l:
                    l+=1
                    continue
                if i == r:
                    r-=1
                    continue
                if abs(nums[r] + nums[l] + nums[i] - target) < abs(closest - target):
                    closest = nums[r] + nums[l] + nums[i]
                if nums[r] + nums[l] == t:
                    return target
                elif nums[r] + nums[l] > t:
                    r-=1
                else:
                    l+=1
                 
        return closest
                    
                
                
        
        