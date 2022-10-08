# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ll = []
        def dfs(root):
            if not root:return

            self.ll.append(root.val)
            dfs(root.right)
            dfs(root.left)
        
        dfs(root)
        self.ll.sort()

        p_sum = [0]
        for num in self.ll:
            p_sum.append(num+p_sum[-1])

        def binS(num):
            l = 0
            r = len(self.ll)-1
            ans = r+1
            while l<=r:
                mid = l + (r-l)//2
                if self.ll[mid] > num:
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1
            
            return ans

        def f(root):
            if not root:return

            idx = binS(root.val)
            # print(root.val, idx, self.ll, p_sum, p_sum[-1]-p_sum[idx])
            root.val = root.val + p_sum[-1]-p_sum[idx]
            # print()

            f(root.left)
            f(root.right)

        f(root)
        return root