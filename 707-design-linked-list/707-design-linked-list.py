class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        node = self.head
        while index and node:
            node = node.next
            index-=1
            
        return -1 if not node else node.val
        
        
    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        
        node = ListNode(val)
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        node = self.head
        while node.next:
            node = node.next
        
        node.next = ListNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            if index != 0: return
            self.head = ListNode(val)
            return
        
        if index == 0:
            node = ListNode(val)
            node.next = self.head
            self.head = node
            return
                
        node = self.head
        while index-1 and node:
            node = node.next
            index -=1
        
        if not node: return 
        new = ListNode(val)
        new.next = node.next
        node.next = new
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        
        node = self.head
        if not node:
            return
        
        while index-1 and node:
            node = node.next
            index -= 1
        
        if not node: return
        node.next = None if not node.next else node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)