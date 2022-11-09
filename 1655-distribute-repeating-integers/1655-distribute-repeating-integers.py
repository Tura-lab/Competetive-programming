class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        n = len(quantity)
        quantity.sort(reverse = True)
        
        counts = sorted(list(Counter(nums).values()))
        freq_count = Counter(counts)
        
        def dfs(i):
            if i == n:
                return True
            
            for freq, count in list(freq_count.items()):
                if freq >= quantity[i] and count > 0:
                    freq_count[freq] -= 1
                    freq_count[freq - quantity[i]] += 1
                    
                    if dfs(i+1): return True
                    
                    freq_count[freq] += 1
                    freq_count[freq - quantity[i]] -= 1
                    
            return False
        
        return dfs(0)