class MyQueue:

    def __init__(self):
        self.que = []
        self.size = len(self.que)

    def push(self, x: int) -> None:
        self.que = [x] + self.que

    def pop(self) -> int:
        popped = self.que[-1]
        self.que = self.que[:-1]
        return popped
    
    def peek(self) -> int:
        return self.que[-1]

    def empty(self) -> bool:
        return len(self.que) ==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
