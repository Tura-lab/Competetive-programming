# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next -1 3 0 4 5
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #THIS SHOULD WORK
        # sorted_head = ListNode(-6000)
        # temp = head
        # while temp:
        #     pos = sorted_head
        #     while pos and temp and pos.val < temp.val:
        #         if pos.next == None:
        #             nxt = temp.next
        #             temp.next = None
        #             pos.next = temp
        #             break
        #         elif pos.next and pos.next.val >= temp.val:
        #             nxt = temp.next
        #             item = pos.next
        #             pos.next = temp
        #             temp.next = item
        #             break
        #         pos = pos.next
        #     temp = nxt
        # return sorted_head.next
        temp = head
        arr=[]
        while temp:
            nxt = temp.next
            temp.next = None
            arr.append(temp)
            temp = nxt
        for i in range(1, len(arr)):
            key = arr[i]
            while i>0 and arr[i-1].val > key.val:
                arr[i]= arr[i-1]
                i-=1
            arr[i] = key
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        return arr[0]
        