# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter()
        mx = 0
        
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            counts[node.val] += 1
            mx = max(mx, counts[node.val])
            stack.append(node.left)
            stack.append(node.right)
            
        return [val for val, count in counts.items() if count == mx]