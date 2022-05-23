import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
            
        return [nums[k] for k in sorted([heapq.heappop(heap)[1] for i in range(k)])]