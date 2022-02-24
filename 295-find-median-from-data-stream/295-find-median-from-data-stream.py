from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = 0

    def addNum(self, num: int) -> None:
        if num > self.median:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
            
        if len(self.minHeap) > 1 + len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.maxHeap) > 1 + len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))
            
        
        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0] + (-self.maxHeap[0]))/2
        elif len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        else:
            self.median = -self.maxHeap[0]

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()