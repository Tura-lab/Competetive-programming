class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        self.mask_dict = defaultdict(int)
        
        def count_bits(mask):
            count = 0
            for i in range(12):
                if mask & 1 << i:
                    count += 1
            return count
        
        def dfs(i, j, mask):
            if i > j:
                cur = count_bits(mask)
                self.mask_dict[mask] = max(self.mask_dict[mask], cur)
                return 
        
            if s[i] == s[j]:
                dfs(i + 1, j - 1, (mask | 1 << i) | 1 << j)
        
            dfs(i + 1, j, mask)
            dfs(i, j - 1, mask)
        
            
        dfs(0, n - 1, 0)
        
        best = 1
        for cur_mask in self.mask_dict.keys():
            for another_mask in self.mask_dict.keys():
                if (another_mask & cur_mask) == 0:
                    best = max(best, self.mask_dict[cur_mask] * self.mask_dict[another_mask])
                
        return best