class Solution:
    def totalNQueens(self, n: int) -> int:
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
                ans.append(1)
                return 
            for row in range(n):
                if isValid([row,col], solution):
                    solution.append(row)
                    solve(ans, solution, col+1)
                    solution.pop()
            return len(ans)

        return solve([])
