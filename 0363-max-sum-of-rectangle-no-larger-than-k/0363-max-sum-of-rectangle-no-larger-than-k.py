class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        best = -float('inf')
        
        for left in range(cols): # fix left col
            cur_sums = [0] * rows
            for right in range(left, cols): # fix right col
                for i in range(rows): # add cur column to sums
                    cur_sums[i] += matrix[i][right]
                
                sorted_sums = [0]
                val = 0
                
                for num in cur_sums:
                    val += num
                    
                    idx = bisect_left(sorted_sums, val - k)
                    
                    if idx < len(sorted_sums) and val - sorted_sums[idx] <= k:
                        best = max(best, val - sorted_sums[idx])
                    
                    bisect.insort(sorted_sums, val)
                        
        return best