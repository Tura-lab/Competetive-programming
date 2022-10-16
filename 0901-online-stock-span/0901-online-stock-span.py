class StockSpanner:
    '''
    [100,80,60,70,60,75,85]
    100, 80,(75,4), 
    '''

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        count = 0
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((price, count+1))

        return count+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)