# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        new_head = head
        
        length = 0
        
        temp = head
        while temp:
            length += 1
            temp = temp.next
            
        k %= length
        
        def dfs(count, node):
            nonlocal new_head
            
            if not node:
                return
            
            dfs(count+1, node.next)
            
            if node.next and count >= length-k:
                node.next.next = new_head
                new_head = node.next
                node.next = None
        
        dfs(1, head)
        
        return new_head