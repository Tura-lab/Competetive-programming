# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        if not nums:
            return None
        root = TreeNode()
        def makeTree(start,end,root):
            mid = (start+end)//2
            root.val = nums[mid]
            if mid-1-start>=0:
                root.left = TreeNode()
                makeTree(start,mid-1,root.left)

            if end-mid-1>=0:
                root.right = TreeNode()
                makeTree(mid+1,end, root.right)
            
        makeTree(0,len(nums)-1,root)
        return root