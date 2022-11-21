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
                    matrix[i][j] = '#'
                    for col in range(cols):
                        if matrix[i][col] != 0:
                            matrix[i][col] = '#'
                    for row in range(rows):
                        if matrix[row][j] != 0:
                            matrix[row][j] = '#'
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
                    
                    