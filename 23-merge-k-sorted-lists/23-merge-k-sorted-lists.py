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
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
        while heap:
            node = heapq.heappop(heap)[-1]
            new.next = node
            if node.next:
                i+=1
                heapq.heappush(heap, (node.next.val, i, node.next))
            new = new.next        
        
        return dummy.next
    
        