class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None]*k
        self.current_length = 0
        self.size = k
        self.front = (self.size//2)-1
        self.last = self.size//2
        
    def insertFront(self, value: int) -> bool:
        if self.current_length +1 >self.size:
            return False
        if self.front == self.size-1:
            self.front = 0
        else:
            self.front+=1
        self.deque[self.front] = value
        self.current_length+=1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.current_length +1 >self.size:
            return False
        if self.last==-self.size:
            self.last = -1
        else:
            self.last-=1
        self.deque[self.last] = value
        self.current_length+=1
        return True

    def deleteFront(self) -> bool:
        if self.current_length==0:
            return False
        self.deque[self.front] = None
        if self.front == -self.size:
            self.front = -1
        else:
            self.front-=1
        self.current_length-=1
        return True

    def deleteLast(self) -> bool:
        if self.current_length==0:
            return False
        self.deque[self.last] = None
        if self.last == self.size-1:
            self.last = 0
        else:
            self.last+=1
        self.current_length-=1
        return True

    def getFront(self) -> int:
        if self.current_length==0:
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.current_length==0:
            return -1
        return self.deque[self.last]

    def isEmpty(self) -> bool:
        return self.current_length==0

    def isFull(self) -> bool:
        return self.current_length==self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
