# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        tree = []
        def inord(root):
            if not root: return
            
            inord(root.left)
            tree.append(root.val)
            inord(root.right)

        inord(root)
        return tree[k-1]
        
        
    
            