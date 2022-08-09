class Solution:
    def numFactoredBinaryTrees(self, nums: List[int]) -> int:
        mod = 10**9 +7
        
        nums.sort()
        pos = set(nums)
        pairs = defaultdict(list)
        for a in nums:
            for b in nums:
                cur = a*b
                if cur in pos:
                    pairs[cur].append((a,b)) 
                    
        # print(dict(pairs))
        
        found = defaultdict(int)
        for num in nums:
            found[num] = 1
            for a,b in pairs[num]:
                found[num] += ((1 if a not in found else found[a])%mod * (1 if b not in found else found[b])%mod)%mod
        
        # print(found)
                
        return 0 if not found else sum(found.values())%mod
    