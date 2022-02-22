import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        self.k = k
        heapq.heapify(self.heap)
        
        for i in range(k, len(nums)):
            if nums[i] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, nums[i])
        
    def add(self, val: int) -> int:
        if len(self.heap)<self.k or val > self.heap[0]:
            if len(self.heap) == self.k:
                heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)