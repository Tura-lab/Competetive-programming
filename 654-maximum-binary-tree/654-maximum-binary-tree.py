# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# import random
class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # nums = [i+1 for i in range(1000)]
        # random.shuffle(nums)
        # print(nums)
        def makeTree(nums):
            if not nums:
                return 
            
            num = max(nums)
            index = nums.index(num)
            
            left  = makeTree(nums[:index])
            right = makeTree(nums[index+1:])
            
            return TreeNode(num, left, right)
        
        return makeTree(nums)