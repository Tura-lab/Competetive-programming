class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        12
        45
        """
        n = len(matrix)
        
        count = 0
        cur_row, cur_col = 0,  n - 1
        i, j = 0, 0
        past = matrix[n - j - 1][i]
        while count < n * n:
            temp = matrix[i][j]
            matrix[i][j] = past
            past = temp
            
            count += 1
            val = count % 4
            
            
            if val == 1 and count != 1:
                if j + 1 == cur_col:
                    cur_row += 1
                    cur_col -= 1
                    i, j = cur_row, cur_row
                else:
                    i, j = i, j + 1
                
                
                past = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                    
                
            if val == 0:
                i, j = j, n - i - 1  
            elif val == 1:
                i, j = j, cur_col
            elif val == 2:
                i, j = j, cur_col - (i - cur_row) 
            else:
                i, j = j, (cur_col - i) + (n - 1 - cur_col )
                    
            # for m in matrix:print(m)
            
        
        
        return matrix