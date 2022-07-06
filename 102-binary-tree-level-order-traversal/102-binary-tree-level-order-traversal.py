# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        #DFS
        def helper(root, level):
            if not root:
                return 
            if len(ans)<=level:
                ans.append([])
            
            ans[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
            
        helper(root, 0)
        return ans
        
#         BFS
#         if not root:
#             return []
#         temp = deque()
#         temp.append(root)
#         ans = []
#         i=0
#         while temp:
#             level = []
#             for i in range(len(temp)):
#                 node = temp.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     temp.append(node.left)
#                 if node.right:
#                     temp.append(node.right)
#             ans.append(level)
        
#         return ans
                
                
        
        
        