class Node:
    def __init__(self, val=None, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = {}
        self.head = None
        self.tail = None
    # def printer(self,head):
    #     while head:
    #         print(head.val, end=',')
    #         head = head.next
    #     print([(i,j.val) for i,j in self.items.items()])
    def get(self, key: int) -> int:
        # print('get', str(key))
        if key in self.items:
            if self.head == self.items[key]:
                # self.printer(self.head)
                return self.items[key].val
            node = self.items[key]
            if node ==self.tail:
                self.tail = node.prev
            if node.next:
                node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
                node.next = self.head
                node.prev=None
                self.head.prev = node
                self.head = node
            else:
                if node.prev:
                    node.prev.next = node.next
                node.next = self.head
                self.head.prev = node
                self.head = node
            # self.printer(self.head)
            return self.items[key].val
        else:
            # self.printer(self.head)
            return -1        
        
    def put(self, key: int, value: int) -> None:
        # print('put', str(key))
        
        if key in self.items:
            self.items[key].val = value
            node = self.items[key]
            if node == self.head:
                return
            if node ==self.tail:
                self.tail = node.prev
            if node.next:
                node.next.prev = node.prev
                if node.prev:
                    node.prev.next = node.next
                node.next = self.head
                node.prev=None
                self.head.prev = node
                self.head = node
            else:
                if node.prev:
                    node.prev.next = node.next
                node.next = self.head
                self.head.prev = node
                self.head = node
            # self.printer(self.head)
        else:
            node = Node(value, key)
            if len(self.items) == 0:
                self.head = self.tail = node
            else:
                if len(self.items) == self.capacity:
                    k = self.tail.key
                    # print(self.items, len(self.items))
                    del self.items[k]
                    if self.capacity!=1:
                        self.tail.prev.next = None
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                    self.tail = self.tail.prev
                    self.tail.next=None
                else:
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
            self.items[key] = node
            # self.printer(self.head)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)