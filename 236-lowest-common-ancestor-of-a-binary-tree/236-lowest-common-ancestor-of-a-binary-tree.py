# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, temp):
            if not node:
                return
            if node.val == target.val:
                path.append(temp + [node])
                # print(path)
                return
            
            temp.append(node)
            dfs(node.left, temp)
            dfs(node.right, temp)
            temp.pop()
            
            
        path = []
        target = p
        dfs(root, [])
        
        target = q
        dfs(root, [])
        
        
        path_for_p = path[0]
        path_for_q = path[1]
        
        for i in range(min(len(path_for_p), len(path_for_q))):
            if path_for_p[i] != path_for_q[i]:
                return path_for_q[i-1]
        
        if len(path_for_p) < len(path_for_q):
            return path_for_p[-1]
        return path_for_q[-1]
            
            
            
            
            
            
            
            