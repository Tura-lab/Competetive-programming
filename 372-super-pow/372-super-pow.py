class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = int(''.join(map(str, b)))
        a = a%1337
        
        def p(num):
            if num<=1:
                return a
            
            ans = p(num//2)%1337
            
            if num%2==0:
                return ((ans) * (ans))%1337
        
        
            return ((a)*(ans)*(ans))%1337
            
                
            
        return p(num)
        # return pow(a, num, 1337)