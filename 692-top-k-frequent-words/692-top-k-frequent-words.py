from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        counts = Counter(nums)
        mapper = {}
        for num, count in counts.items():
            if count in mapper:
                mapper[count].append(num)
            else:
                mapper[count] = [num]
                
        for count, nums in mapper.items():
            nums.sort()
        minHeap = []
        heapq.heapify(minHeap)

        for count, nums in mapper.items():
            for i in range(len(nums)):
                if len(minHeap) == k:
                    if minHeap[0] < counts[nums[i]]:
                        heapq.heappop(minHeap)
                        heapq.heappush(minHeap, count)

                else:
                    heapq.heappush(minHeap, count)

        ans = []
        minHeap = list(set(minHeap))
        minHeap.sort(reverse=True)
        for i in range(len(minHeap)):
            if len(ans)==k:
                break
            for i in mapper[minHeap[i]]:
                if len(ans)==k:
                    break
                ans.append(i)

        return ans