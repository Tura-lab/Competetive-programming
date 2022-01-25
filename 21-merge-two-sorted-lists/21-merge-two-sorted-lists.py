# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Linked_list:
    def __init__(self):
        self.head = None
            
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val > l2.val:
            new = l2
            l2 = l2.next
        else:
            new = l1
            l1 = l1.next
        head = new
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
        rem = l1 or l2
        while rem:
            new.next = rem
            rem = rem.next
            new = new.next
        return head
