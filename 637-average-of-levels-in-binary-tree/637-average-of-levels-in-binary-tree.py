# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = collections.deque()
        q.append(root)
        
        while q:
            tot=num=0
            for i in range(len(q)):
                node = q.popleft()
                tot+=node.val
                num+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            ans.append(tot/num)
        return ans            
            
            