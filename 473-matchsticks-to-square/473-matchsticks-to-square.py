class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 !=0: return False
        
        side = total//4
        
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        
        @cache
        def solve(i,t,r,b,l):
            count=0
            if t==side: count += 1
            if r==side: count += 1
            if b==side: count += 1
            if l==side: count += 1
                
            if count == 3:
                return True
            if t>side or r>side or b>side or l>side: return False
            
            return solve(i+1, t + matchsticks[i], r, b, l) or solve(i+1, t, r + matchsticks[i], b, l) or solve(i+1, t, r, b + matchsticks[i], l) or solve(i+1, t, r, b, l + matchsticks[i])
        
        return solve(0,0,0,0,0)