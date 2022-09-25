class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows,cols = len(heights), len(heights[0])

        def dfs(row, col):
            if (row,col) in visited:return
            
            visited.add((row,col))
            for a,b in [[-1,0],[1,0],[0,1],[0,-1]]:
                if -1<row+a<rows and -1<col+b<cols and heights[row+a][col+b] >= heights[row][col]:
                    dfs(row+a, col+b)
                
        visited=set()
        for i in range(rows):
            dfs(i, 0)
        for j in range(cols):
            dfs(0, j)
        
        found = set(visited)
        
        visited=set()
        for i in range(rows):
            dfs(i, cols-1)
        for j in range(cols):
            dfs(rows-1, j)
        
        ans = []
        
        for cell in visited:
            if cell in found:
                ans.append(cell)
                
        return ans