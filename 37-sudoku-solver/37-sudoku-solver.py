class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, num):
            if num in rows[row]:
                return False
            if num in cols[col]:
                return False
            
            while row% 3!= 0:
                row -= 1
            while col%3!=0:
                col-=1
                
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if str(num) == b[i][j]:
                        return False
            
            
            return True
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        emptys = []
        
        for row in range(9):
            for col in range(9):
                val = b[row][col]
                if val == '.':
                    emptys.append((row,col))
                    continue
                rows[row].add(val)
                cols[col].add(val)


        self.ans = []
        def solve(idx, ans):
            if len(ans) == len(emptys):
                self.ans = ans[:]
                return 
            
            # print(idx,emptys[idx], len(emptys))
            row,col = emptys[idx]
            
            for num in range(1,10):
                num = str(num)
                if isValid(row,col,num):
                    rows[row].add(num)
                    cols[col].add(num)
                    b[row][col] = num
                    
                    solve(idx+1,ans + [num])
                    
                    rows[row].remove(num)
                    cols[col].remove(num)
                    b[row][col] = '.'

        
        solve(0, [])
        k=0
        for i in range(9):
            for j in range(9):
                if b[i][j] == '.':
                    b[i][j] = self.ans[k]
                    k+=1
        return b  