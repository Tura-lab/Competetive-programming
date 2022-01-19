class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        # print('get')
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        temp = self.head
        i=0
        while temp:
            if i == index:
                return temp.val
            temp = temp.next
            i+=1
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        return -1
    def addAtHead(self, val: int) -> None:
        # print('addAtHead')
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        nxt = self.head
        self.head = ListNode(val, nxt)
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
    def addAtTail(self, val: int) -> None:
        if self.head ==None:
            self.head = ListNode(val)
            return
        # print('addAtTail')
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = ListNode(val)
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
    def addAtIndex(self, index: int, val: int) -> None:
        # print('addAtindex')
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        if index ==0:
            self.head = ListNode(val, self.head)
            return
        i=0
        temp=self.head
        while temp:
            if i == index-1:
                temp.next = ListNode(val, temp.next)
                break
            temp = temp.next
            i+=1
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        if index==0:
            self.head = self.head.next
            return
        # print('deleteAtIndex')
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        i=0
        temp = self.head
        while temp:
            if i==index-1:
                if temp.next:
                    temp.next = temp.next.next
                else:
                    temp.next = None
                break
            temp = temp.next
            i+=1
        # t = self.head
        # while t:
        #     print(t.val, end= '*')
        #     t = t.next
        # print()
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)