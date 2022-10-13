# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:return TreeNode(val)
        node = None
        h = root
        while root:
            node = root
            root = root.right if root.val < val else root.left
        
        if node.val > val:
            node.left = TreeNode(val)
        else:
            node.right = TreeNode(val)
            
        return h
            