class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row, col = len(strs), len(strs[0])
        
        count = 0
        for i in range(col):
            for j in range(1, row):
                if strs[j-1][i] > strs[j][i]:
                    count += 1
                    break
        
        return count