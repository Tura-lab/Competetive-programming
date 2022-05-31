# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = head
        e = head
        if not head:
            return
        odd = head.next
        o = odd
        
        while even and odd and even.next and odd.next:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        
        even.next = o
        return e