# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Linked_List:
#     def __init__(self):
#         self.head = None

class Solution:
    def merge(self,l1,l2):
        new = ListNode()
        h=new
        while l1 and l2:
            if l1.val> l2.val:
                new.next = l2
                l2 = l2.next
            else:
                new.next = l1
                l1 = l1.next
            new = new.next
        new.next = l1 or l2
        return h.next
    def merger(self, lists, start, end):
        if start==end:
            return lists[start]
        mid = (start+end)//2
        left = self.merger(lists, start,mid)
        right = self.merger(lists, mid+1, end)
        return self.merge(left,right)
    
    def mergeKLists(self, lists):
        if lists==[]:
            return None
        return self.merger(lists, 0, len(lists)-1)
    
    
    
    
    
    
    
    
    
    
    
        # ls = []
        # for l in lists:
        #     temp = l
        #     while temp:
        #         ls.append(temp.val)
        #         temp = temp.next
        # if ls == []:
        #     return None
        # final_LL = Linked_List()
        # ls = sorted(ls)
        # final_LL.head = ListNode(ls[0])
        # current = final_LL.head
        # for i in ls[1:]:
        #     current.next = ListNode(i)
        #     current = current.next
        # return final_LL.head
        