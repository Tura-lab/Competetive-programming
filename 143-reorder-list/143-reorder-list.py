# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4
# 9 8 7 6 5

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        fast = slow = head
        past = None
        while fast and fast.next:
            fast = fast.next.next
            past = slow
            slow = slow.next
        prev = None
        if past:
            past.next = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head2 = prev
        new = ListNode()
        while head2 and head:
            nxt = head.next
            nxt2 = head2.next
            new.next = head
            new = new.next
            new.next = head2
            head, head2, new = nxt, nxt2, new.next
                
        