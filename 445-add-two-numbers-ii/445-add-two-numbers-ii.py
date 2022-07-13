# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        
        temp = l1
        len1 = 0
        while temp:
            num1.append(temp.val)
            temp = temp.next
            len1 +=1
        
        temp = l2
        len2 = 0
        while temp:
            num2.append(temp.val)
            temp = temp.next
            len2 +=1
        
        node = l1 if len1>len2 else l2
        stack = []
        
        temp = node
        while temp:
            stack.append(temp)
            temp = temp.next
        
        carry = 0
        while num1 or num2:
            add = carry + (0 if not num1 else num1.pop()) + (0 if not num2 else num2.pop())
            stack[-1].val = add%10
            
            carry = add//10
            stack.pop()        
        if carry:
            return ListNode(carry, node)
        
        return node
        