# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''

    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new = ListNode()
        h=new
        temp = head
        i=0
        while temp and temp.next :
            if temp.val == temp.next.val:
                while temp and temp.next and temp.val == temp.next.val:
                    temp= temp.next
                temp = temp.next
                new.next = temp
            else:
                new.next = temp
                new = new.next
                temp=temp.next  
        return h.next