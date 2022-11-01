# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        ans = []
        self.idx = 0
        self.good = True
        def dfs(node, parent):
            if not node:return
            
            if node.val != voyage[self.idx]:
                if not parent:
                    self.good = False
                    return 
                if parent.right and voyage[self.idx] == parent.right.val:
                    parent.right, parent.left = parent.left, parent.right
                    node = parent.left
                    ans.append(parent.val)
                else:
                    self.good = False
                    return
            
            self.idx += 1
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
            
        if self.good:
            return ans
        return [-1]