# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = [None,None,None]
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if nodes[0] and nodes[0].val > root.val:
                if not nodes[1]:
                    nodes[1] = nodes[0]
                nodes[2] = root
            nodes[0] = root
            dfs(root.right)        
        
        dfs(root)
        nodes[1].val, nodes[2].val = nodes[2].val, nodes[1].val
        