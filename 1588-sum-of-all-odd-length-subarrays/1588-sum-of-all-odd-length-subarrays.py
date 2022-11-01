class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        p_sum = [0]
        for num in arr:
            p_sum.append(p_sum[-1]+num)
            
        total = 0
        start = 0
        for i in range(1, len(p_sum)):
            
            for j in range(start, i, 2):
                total += p_sum[i] - p_sum[j]
            
            start = 1-start
        
        return total