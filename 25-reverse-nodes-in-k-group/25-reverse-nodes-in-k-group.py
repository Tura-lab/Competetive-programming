# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k<=1 or not head:
            return head
        new = ListNode()
        end = new
        temp = head
        length = 0
        while temp:
            length+=1
            temp = temp.next
        tot = length//k
        i = 0
        cur = head
        while i<tot:
            prev = None
            j=0
            temp = cur
            while cur and j<k:
                nxt = cur.next
                cur.next = prev
                prev =  cur
                cur = nxt 
                j+=1
            end.next = prev
            end = temp
            i+=1
        end.next = nxt
        return new.next