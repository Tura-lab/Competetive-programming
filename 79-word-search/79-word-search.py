class Solution:
    '''
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        
        def dfs(i, j, k):
            if k ==len(word):
                return True
            if not(-1<i<row and -1<j<col) or word[k] != board[i][j] or board[i][j]=='-':
                return False
            
            t = board[i][j]
            board[i][j]='-'
            
            ans = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            
            board[i][j] = t
            return ans

        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j]:
                    if dfs(i,j,0):
                        return True
                    
        return False