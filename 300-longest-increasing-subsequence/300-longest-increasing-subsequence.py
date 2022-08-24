class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        
        for num in nums:
            if not ans or ans[-1]<num:
                ans.append(num)
            else:
                l = 0
                r = len(ans)-1
                
                pos=0
                while l<=r:
                    mid = l + (r-l)//2
                    
                    if ans[mid] >= num:
                        pos = mid
                        r = mid-1
                    else:
                        l = mid+1
        
                ans[pos] = num
        
        return len(ans)