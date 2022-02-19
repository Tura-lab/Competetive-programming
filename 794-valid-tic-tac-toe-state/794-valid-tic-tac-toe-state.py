class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        board = ''.join(board)
        count = 0
        x=0
        o=0
        for i in board:
            if i != ' ':
                if i == 'O':
                    o+=1
                if i == 'X':
                    x+=1
                count+=1

        def gameOver(s):
            for i in range(0,7,3):
                if board[i]==board[i+1]==board[i+2]==s:
                    return True
            for i in range(3):
                if board[i]==board[i+3]==board[i+6]==s:
                    return True
            if board[0]==board[4]==board[8]==s:
                return True
            if board[2]==board[4]==board[6]==s:
                return True
            
            return False
        winx = gameOver('X')
        wino = gameOver('O')
        if abs(x-o)>1 or o>x or (winx and wino):
            return False
        if (winx and x!=o+1) or (wino and x!=o):
            return False
        return True
        
            
