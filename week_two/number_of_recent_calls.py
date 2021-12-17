class RecentCounter:

    def __init__(self):
        self.calls = []
        self.count = 0
        self.start = 0

    def ping(self, t: int) -> int:
        self.calls.append(t)
        self.count+=1
        i = self.start
        if self.calls[i]>=t-3000:
            return self.count - i
        while i<self.count:
            if self.calls[i]>=t-3000:
                self.start=i
                return self.count - i
            i+=1
            

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
