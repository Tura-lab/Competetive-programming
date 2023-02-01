class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        
        count = 0
        i = 0
        for j in range(len(blocks)):
            count += blocks[j] == 'W'
            
            if j-i+1 > k:
                count -= blocks[i] == 'W'
                i += 1
                
            if j-i+1 == k:
                ans = min(ans, count)
        
        return ans