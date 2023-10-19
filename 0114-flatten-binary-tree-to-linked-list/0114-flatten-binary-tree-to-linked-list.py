# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.start = None
        self.head = None
        original = self.head
        
        if self.head:
            self.head.right = None
            self.head.left = None
        
        def dfs(root):
            if not root:
                return
            
            l, r = root.left, root.right
            
            root.left = None
            root.right = None
            if self.head:
                self.head.right = root
                self.head = self.head.right
            else:
                self.head = root
                self.start = self.head
            self.head = root
            
            dfs(l)
            dfs(r)
        
        dfs(root)
        cur = original

        
        root = self.start
        
        # return None if original == None else original.right