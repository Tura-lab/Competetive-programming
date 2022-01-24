# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4 5 6 7 8
                i
        j
'''  
class Solution:
    # O(1) -> space
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        fast = slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next
        cur = slow
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head2 = prev
        while head2:
            ans = max(ans, head.val + head2.val)
            head = head.next
            head2 = head2.next
        return ans
    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     arr = []
    #     temp = head
    #     while temp:
    #         arr.append(temp.val)
    #         temp = temp.next
    #     i=0
    #     j = len(arr)-1
    #     ans = 0
    #     while i<j:
    #         ans = max(ans, arr[i] + arr[j])
    #         i+=1
    #         j-=1
    #     return ans
        