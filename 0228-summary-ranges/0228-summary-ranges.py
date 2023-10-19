class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end = None, None
        
        cur = None
        ans = []
        
        for i, num in enumerate(nums):
            if cur == None:
                cur = num
                
            if num == cur:
                if start == None:
                    start = end = cur
                else:
                    end = cur
                cur += 1
                    
            else:
                ans.append(f"{start}->{end}" if start != end else str(start))
                start = end = cur = num
                cur += 1
                
                
        if start != None:
            ans.append(f"{start}->{end}" if start != end else str(start))
            
        return ans