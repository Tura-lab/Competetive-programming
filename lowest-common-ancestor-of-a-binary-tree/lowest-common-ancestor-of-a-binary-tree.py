# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if root == None or root==q or root==p:
                return root
            
            leftSearch = helper(root.left)
            rightSearch = helper(root.right)
            
            if rightSearch and leftSearch:
                return root
            return leftSearch or rightSearch
                
        return helper(root)
        
        
#         BAADDD
#         roots = []
        
#         def helper(root, arr):
#             if not root:
#                 return
#             if root == p:
#                 roots.append (arr + [p])
#             if root == q:
#                 roots.append(arr + [q])
            
#             helper(root.left, arr+[root])
#             helper(root.right, arr+[root])
        
#         helper(root, [])
        
#         set1 =set(roots[0])
#         for i in range(len(roots[1])-1,-1,-1):
#             node = roots[1][i]
#             if node in set1:
#                 return node