# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        def dfs(node, h):
            if not node:return
            if h==0:
                left = TreeNode(val, node.left, None)
                right = TreeNode(val, None, node.right)
                node.right = right
                node.left = left
                return 
            
            dfs(node.left, h-1)
            dfs(node.right, h-1)
            
        dfs(root, depth-2)
        return root