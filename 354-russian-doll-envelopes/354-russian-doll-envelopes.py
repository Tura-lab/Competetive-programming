class Solution:
    def maxEnvelopes(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: (x[0], -x[1]))
        # print(nums)
        
        n = len(nums)
        ans = []
        '''
        1, 2, 1, 
        '''
        
        for w,h in nums:
            if not ans or h>ans[-1]:
                ans.append(h)
            else:
                l = 0
                r = len(ans)-1
                
                pos=0
                while l<=r:
                    mid = l + (r-l)//2
                    
                    if ans[mid]>=h:
                        pos = mid
                        r = mid-1
                    else:
                        l = mid+1
        
                ans[pos] = h
            # print(ans)
        
        # print(ans)
        return len(ans)