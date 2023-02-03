# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        found = defaultdict(list)
        
        rows_start, cols_start = 0, 0
        rows, cols = 0, 0
        
        def dfs(node, row, col):
            nonlocal rows_start, rows, cols_start, cols
            
            if not node:
                return 
            
            rows_start = min(rows_start, row)
            rows = max(rows, row)
            
            cols_start = min(cols_start, col)
            cols = max(cols, col)
            
            found[(row, col)].append(node.val)
            
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
            
            
        dfs(root, 0, 0)
        
        ans = []
        
        # print(dict(found))
        
        for c in range(cols_start, cols + 1):
            col = []
            for r in range(rows_start, rows + 1):
                for val in sorted(found[(r, c)]):
                    col.append(val)
                    
                    
            ans.append(col)
            
            
        return ans
            
            
            
            
            
            