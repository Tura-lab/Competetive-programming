from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.d = deque()

    def enQueue(self, value: int) -> bool:
        if len(self.d) == self.size:return
        self.d.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.d:return
        self.d.popleft()
        return True

    def Front(self) -> int:
        if not self.d:return -1
        return self.d[0]

    def Rear(self) -> int:
        if not self.d:return -1
        return self.d[-1]

    def isEmpty(self) -> bool:
        return not self.d

    def isFull(self) -> bool:
        return len(self.d) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()