# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    2 1 3
    2 3 1
    '''
    def buildTree(self, inorder, postorder):
        if not postorder or not inorder:
            return
        node = TreeNode(postorder[-1])
        idx = inorder.index(node.val)
        
        node.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        node.left = self.buildTree(inorder[:idx], postorder[:idx])
    
        return node