class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        counts_perside = n // 3
        
        ans = float('inf')
        heap = []
        left_min = []
        # find smallest sum before every idx 
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            heappush(heap, -num)
            
            while heap and len(heap) > counts_perside:
                num = -heappop(heap)
                cur_sum -= num
            left_min.append(cur_sum if len(heap) == counts_perside else float('inf'))
            
        # find biggest sum after every idx 
        heap = []
        cur_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            
            if len(heap) == counts_perside:
                ans = min(ans, left_min[i] - cur_sum)
            
            cur_sum += num
            heappush(heap, num)
            
            while heap and len(heap) > counts_perside:
                num = heappop(heap)
                cur_sum -= num
                
        return ans