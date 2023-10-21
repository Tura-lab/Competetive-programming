# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        5, 3, 2
        5, 6
        """
        self.minStack = []
        self.maxStack = []
        
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left
                
        def push_right(node, stack):
            while node:
                stack.append(node)
                node = node.right
                
        push_left(root, self.minStack)
        push_right(root, self.maxStack)
        
        while self.minStack and self.maxStack:
            while self.minStack and self.maxStack and self.minStack[-1].val + self.maxStack[-1].val > k:
                node = self.maxStack.pop()
                push_right(node.left, self.maxStack)
            while self.minStack and self.maxStack and self.minStack[-1].val + self.maxStack[-1].val < k:
                node = self.minStack.pop()
                push_left(node.right, self.minStack)
                
            if self.minStack and self.maxStack and self.minStack[-1] == self.maxStack[-1]:
                break
            if self.minStack and self.maxStack and self.minStack[-1].val + self.maxStack[-1].val == k:
                return True
            
        return False