class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        i = 0 #row
        j = column-1 #column
        
        while -1<i<row and -1<j<column:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]  < target:
                i+=1
            else:
                j-=1
        
        return False