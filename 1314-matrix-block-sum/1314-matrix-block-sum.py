class Solution:
    def matrixBlockSum(self, nums: List[List[int]], k: int) -> List[List[int]]:
        '''
        [1,2,3]
        [4,5,6]
        [7,8,9]
        '''
        
        rows, cols = len(nums), len(nums[0])
        new = [[0] * cols for _ in range(rows)] 
        
        def add(row, col):
            
            total = 0
            for i in range(max(0, row-k), min(row+k+1, rows)):
                for j in range(max(0, col-k), min(col+k+1, cols)):
                    total += nums[i][j]
            
            return total
        
        for i in range(rows):
            for j in range(cols):
                new[i][j] = add(i,j)
                
        return new