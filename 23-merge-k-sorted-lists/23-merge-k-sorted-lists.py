# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Linked_List:
#     def __init__(self):
#         self.head = None
import heapq

class Solution:

    def mergeKLists(self, lists):
        dummy = ListNode()
        new = dummy
        
        heap = []
        heapq.heapify(heap)
        
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
                
        while heap:
            new.next = ListNode(heapq.heappop(heap))
            new = new.next
        
        
        
        return dummy.next
    
        