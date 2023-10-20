# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur_smallest = float('-inf')

    def next(self) -> int:
        def dfs(node):
            if not node:
                return 
                
            if node.val > self.cur_smallest:
                new = dfs(node.left)
                if new != None:
                    return new
                return node.val
            else:
                return dfs(node.right)
                
        self.cur_smallest = dfs(self.root)
        return self.cur_smallest

    def hasNext(self) -> bool:
        def dfs(node):
            if not node:
                return False
            
            if node.val > self.cur_smallest:
                return True
            
            return dfs(node.right)

        return dfs(self.root)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()