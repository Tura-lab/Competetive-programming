class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        h = 29
        
        ans = 0
        p, mod = n+1, 2**63 - 1
        
        if not p&1:
            p+=1
        
        def check(size):
            power = pow(p, size, mod)
            
            counts = Counter()
            for path in paths:
                found = set()   
                code = 0
                for i in range(size):
                    code = (code * p + path[i]) % mod
                
                counts[code] += 1
                found.add(code)
                
                i = 0
                for j in range(size, len(path)):
                    code = (code * p + path[j] - path[i] * power) % mod
                    i += 1
                    if code not in found:
                        found.add(code)
                        counts[code] += 1
            
            return any(count == len(paths) for count in counts.values())
        
        l, r = 1, min(len(path) for path in paths)        
        while l <= r:
            mid = l + (r-l)//2
            
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        
        return ans