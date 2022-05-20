class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        
        def validBox(row, col, num):
            i = row
            j = col
            while i % 3!=0:
                i-=1
            
            while j%3!=0:
                j-=1
                
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if not (k==row and l==col):
                        if board[k][l] == num:
                            return False
            return True
        
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] != '.':
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in cols[col]:
                        return False

                    if not validBox(row,col,board[row][col]):
                        return False
                
                
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                
        
            
        return True
        