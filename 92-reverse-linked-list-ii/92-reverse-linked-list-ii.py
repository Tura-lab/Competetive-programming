# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # def showNodes(node):
        #     found = set()
        #     while node and node not in found:
        #         print(node.val, end='-')
        #         found.add(node)
        #         node = node.next
        #     print(node.val if node else '')
        if left==right:return head
            
        cur = head
        prev = start = None
        pos = 1
        while cur and pos<=right:
            if pos < left:
                pos += 1
                prev = cur
                start = prev
                cur = cur.next
                continue
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            pos += 1
            
        # showNodes(head)
        if start:
            if start.next:
                start.next.next = cur
            start.next = prev
        
        if not start:
            head.next = nxt
            head = prev
        # showNodes(head)
        return head
            
            
        