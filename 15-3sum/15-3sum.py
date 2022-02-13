class Solution:
    '''
    -1,0,1,2,-1,-4
    -4,-1,-1,0,1,2
    -4 (4) -> 
    -1 (1) -> -1,2
    -1 (1) -> 
     0 (0) -> 
     1 (-1) ->  

    -1,0,1,2,-1,-4
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(len(nums))
        ans = []
        found = set()
        nums.sort()
        
        for i in range(len(nums)):
            target = 0 - nums[i]
            l=0
            r = len(nums)-1
            
            while l<r:
                if i == l:
                    l+=1
                    continue
                if i == r:
                    r-=1
                    continue
                
                if nums[r] + nums[l] == target:
                    arr = [nums[i], nums[l], nums[r]]
                    arr.sort()
                    arr = tuple(arr)
                    if arr not in found:
                        found.add(arr)
                        ans.append(arr)
                    l+=1
                    r-=1
                elif nums[r] + nums[l] > target:
                    r-=1
                else:
                    l+=1
        return ans
                    
                
                
        
        