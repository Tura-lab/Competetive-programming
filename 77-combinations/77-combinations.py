class Solution:
    def __init__(self):
        self.ans = []
        
    def combiner(self, nums, cur, l):
        if len(cur)==l:
            self.ans.append(cur)
            return
        # if len(nums)==0:
        #     return
        if len(cur) + len(nums) < l:
            return
        self.combiner(nums[1:], cur + [nums[0]], l) #Include
        self.combiner(nums[1:], cur, l) #Exclude
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        self.combiner(nums, [], k)
        
        return self.ans