# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
     1 -> 2
    '''
    def reverseList(self, head, prev=None):
        if head==None:
            return
        if head.next == None:
            head.next = prev
            return head
        nxt = head.next
        head.next = prev
        return self.reverseList(nxt, head)

        
        #Iterative
        # prev = None
        # curr = head
        # while curr is not None:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # head = prev
        # return head
    