class Solution:
    def countPrimes(self, n: int) -> int:
        old = n
        if old <= 1:return 0
        
        isPrime = [True] * (old)
        isPrime[0] = False
        isPrime[1] = False
        
        ans = []
        i=2
        while i*i <= old:
            if isPrime[i]:
                j = i*i
                while j < old:
                    isPrime[j] = False
                    j+=i

            i+=1
        
        count = 0
        for num in isPrime:
            count += num
        
        return count