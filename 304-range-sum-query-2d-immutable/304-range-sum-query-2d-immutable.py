class NumMatrix:
    '''
      5  6  3  2  1
    0 5 11 14 16 17
    
    '''

    def __init__(self, matrix: List[List[int]]):
        pre_sum=[]
        i=0
        for row in matrix:
            arr = [0]
            for i in row:
                arr.append(arr[-1]+i)
            pre_sum.append(arr)
        
        self.matrix = pre_sum        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        j=row1
        ans=0
        while j<=row2:
            ans += (self.matrix[j][col2+1]-self.matrix[j][col1])
            j+=1
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)