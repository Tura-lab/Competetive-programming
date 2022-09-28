class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        [9,8,1,0,1,9,4,0,4,1]
        '''
        ans = -float('inf')
        found = [(nums[-1], len(nums)-1)]
        
        def find(num):
            l = 0
            r = len(found)-1
            while l<=r:
                mid = l + (r-l)//2
                if found[mid][0] >= num:
                    ans = found[mid][1]
                    r = mid-1
                else:
                    l = mid+1
                    
            return ans
                
        
        for i in range(len(nums)-2, -1, -1):
            if found[-1][0] < nums[i]:
                found.append((nums[i], i))
            # print(nums[i],found)
            ans = max(ans, find(nums[i])-i)
                
        return ans