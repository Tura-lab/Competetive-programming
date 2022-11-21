class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        done_rows, done_cols = set(), set()
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    done_rows.add(i)
                    done_cols.add(j)
        
        for i in done_rows:
            for j in range(cols):
                matrix[i][j] = 0
        
        for j in done_cols:
            for i in range(rows):
                matrix[i][j] = 0
                
        
        