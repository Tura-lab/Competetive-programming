class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        rows, cols = len(board), len(board[0])
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        
        def in_bound(row,col):
            return -1 < row < rows and -1 < col < cols
        
        dead = []
        live = []
        
        for row in range(rows):
            for col in range(cols):
                live_count = 0
                for a,b in directions:
                    nx, ny = row+a, col+b
                    if in_bound(nx, ny):
                        live_count += board[nx][ny] == 1
            
                if live_count < 2 and board[row][col] == 1:
                    dead.append((row,col))
                elif live_count > 3 and board[row][col] == 1:
                    dead.append((row, col))
                elif live_count == 3 and board[row][col] == 0:
                    live.append((row,col))
        
        for row, col in dead: board[row][col] = 0
        for row, col in live: board[row][col] = 1
            
            