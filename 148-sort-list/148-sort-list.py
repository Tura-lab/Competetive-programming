# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def printer(head):
        #     while head:
        #         print(f'{head.val} -> ', end = '')
        #         head = head.next
        #     print()
        '''
        1 - 2
            |
               |
        '''
            
        # print(length)
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            fast = slow = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            
            l = merge_sort(head)
            r = merge_sort(slow)
            
            t = ListNode()
            temp = t

            while l and r:
                if l.val < r.val:
                    nxt = l.next
                    temp.next = l
                    l = nxt
                else:
                    nxt = r.next
                    temp.next = r
                    r=nxt
                temp = temp.next
            
            if r: temp.next = r
            if l: temp.next = l
                        
            return t.next
        
        return merge_sort(head)