# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = None
        bigger = None
        first_small = None
        first_big = None
        
        while head:
            nxt = head.next
            head.next = None
            if head.val < x:
                if smaller:
                    smaller.next = head
                    smaller = smaller.next
                else:
                    smaller = head
                    first_small = smaller
                    
            else:
                if bigger:
                    bigger.next = head
                    bigger = bigger.next
                else:
                    bigger = head
                    first_big = bigger
                    
            head = nxt
        
        
        if first_small:
            smaller.next = first_big
            return first_small
        
        
        
        return first_big