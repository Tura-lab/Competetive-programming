class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) #column length
        n = len(matrix) #row length
        i=0 # row
        j = m-1 #column
        while  -1<j<m and -1<i<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i+=1
            elif matrix[i][j] > target:
                j-=1
        return False
            