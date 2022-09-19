class Solution:
    def minimumMoney(self, nums: List[List[int]]) -> int:
        '''
        [[2,1],[5,0],[4,2]]
        
        '''
        earn = []
        lose = []
        for a, b in nums:
            if b>=a:
                earn.append([a,b])
            else:
                lose.append([a,b])
        
        def check(num):
            for a,b in lose:
                if num<a:return False
                num -= a
                num += b
            
            for a,b in earn:
                if num<a:return False
                num -= a
                num += b
            
            return True
                
        
        l = 0
        r = 0
        for a, b in nums:
            r += a
        
        earn.sort(reverse=True)
        lose.sort(key = lambda x: x[1])
        
        ans = r
        while l<=r:
            
            mid = l + (r-l)//2
            
            if check(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        
        return ans