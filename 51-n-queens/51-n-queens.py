class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:            
        
        def isValid(square, solution):
            i,j = square
            if not solution:
                return True
            if i in solution:
                return False
            row = i
            col = j
            while row>-1 and col>-1:
                if -1<col<len(solution) and row == solution[col]:
                    return False
                row-=1
                col-=1
            row = i
            col = j
            while row<n and col>-1:
                if -1<col<len(solution) and row == solution[col]:
                    return False
                row+=1
                col-=1
            return True
        
        def solve(ans,solution=[], col=0):
            if len(solution) == n:
                ans.append(solution[:])
                return
            for row in range(n):
                if isValid([row,col], solution):
                    solution.append(row)
                    solve(ans, solution, col+1)
                    solution.pop()
            return ans

        solved = solve([])
        
        final = []
        for ans in solved:
            board = [''*n]*n
            for i in range(n):
                board[ans[i]] = '.'*i + 'Q' + '.'*(n-i-1)
            final.append(board)
        return final
    
    
    
    
    
    
    
    
    
    
    