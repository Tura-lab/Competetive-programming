class Solution:
    """
             1,5
             
             
     1                   5
    """
    def game(self, nums, start, end, score, i):
        if start==end:
            return i * nums[start]
        left = self.game(nums, start+1, end, score, -i)
        right = self.game(nums, start, end-1, score, -i)
        if i==1:
            return max(left + nums[start], right + nums[end])
        else:
            return min(left - nums[start], right - nums[end])
    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.game(nums, 0, len(nums)-1, 0, 1) >= 0 