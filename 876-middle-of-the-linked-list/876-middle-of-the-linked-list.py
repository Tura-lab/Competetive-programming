# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Obvious approach
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     temp = head
    #     arr=[]
    #     while temp:
    #         arr.append(temp)
    #         temp = temp.next
    #     return arr[len(arr)//2]
    
    # faster
    def middleNode(self, head):
        hare = head
        turt = head
        while hare and hare.next:
            hare = hare.next.next
            turt = turt.next
        return turt
            