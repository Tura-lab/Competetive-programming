class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        self.ans = False
        
        word_count = Counter(word)
        counter  = defaultdict(int)
        
        for a in board:
            for b in a:
                counter[b] += 1
        
        for w in word:
            if word_count[w] > counter[w]:
                return False
        
        
        def dfs(i, j, k):
            if k ==len(word):
                self.ans = True
                return True
            if not(-1<i<row and -1<j<col) or word[k] != board[i][j] or board[i][j]=='-':
                return False
            
            if self.ans:return True
            
            t = board[i][j]
            board[i][j] = -1
            
            ans = dfs(i-1,j,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1)
            
            board[i][j] = t
            return ans

        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j]:
                    dfs(i,j,0)
                    if self.ans:
                        return True
                    
        return False