class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        ans = []
        
        def binS(num):
            ans = None
            
            l = 0
            r = len(potions)-1
            while l<=r:
                mid = l + (r-l)//2
                if num*potions[mid] >= success:
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1
            
            return ans
        
        for num in spells:
            cur = binS(num)
            ans.append(0 if cur==None else len(potions)-cur)
            
        return ans