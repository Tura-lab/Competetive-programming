# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        p = None
        while root:
            if root.val < key:
                p = root
                root = root.right
            elif root.val > key:
                p = root
                root = root.left
            else: 
                if not p:
                    if not root.right:
                        return root.left
                    left = root.left
                    new = root.right
                    root = root.right
                    while root and root.left:
                        root  = root.left
                    if root:
                        root.left = left
                    return new
                elif root == p.left:
                    left = root.left
                    if not root.right:
                        p.left = root.left
                        break
                    p.left = root.right
                    root = root.right
                    while root and root.left:
                        root = root.left
                    if root:
                        root.left = left
                elif root == p.right:
                    left = root.left
                    if not root.right:
                        p.right = root.left
                        break
                    p.right = root.right
                    root = root.right
                    while root and root.left:
                        root = root.left
                    if root:
                        root.left = left
                break
                
        return node
                    
                    
                        
                    
