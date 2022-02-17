# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode()
        l = node
        temp = head
        while temp:
            nxt = temp.next
            if temp.val != val:
                node.next = temp
                temp.next = None
                node = node.next
            temp = nxt
        
        return l.next