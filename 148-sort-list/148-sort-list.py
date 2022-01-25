# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 

class Solution:
    def merge(self, head, slow):
        if head.val > slow.val:
            new = slow
            slow = slow.next
        else:
            new = head
            head = head.next
        h=new
        while head and slow:
            if slow.val < head.val:
                new.next = slow
                slow = slow.next
            else:
                new.next = head
                head = head.next
            new = new.next
        new.next = head or slow
        head=h
        return head
    
    def findMid(self,head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            past = slow
            slow = slow.next
        past.next = None
        return head, slow
    
    def mergeSort(self,head):
        if head and head.next:
            head, slow = self.findMid(head)
            left = self.mergeSort(head)
            right = self.mergeSort(slow)
            return self.merge(left,right)
        else:
            h=head
            return head
        
    def sortList(self, head):
        return self.mergeSort(head)
                