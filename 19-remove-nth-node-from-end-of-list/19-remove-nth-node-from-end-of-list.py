# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        count = 0
        while count <= n:
            if not fast:
                head = head.next
                return head
            fast = fast.next
            count += 1
            
        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return head
        