class Solution:
    '''
    p([1,2], [])
        p([1,2], [1])
            p([1,2], [1,2])
        p([1,2], [2])
            p([1,2], [2,1])
    '''
    def __init__(self):
        self.ans = []
    def helper(self, nums, cur):
        if len(cur) == len(nums):
            self.ans.append(cur)
            return
        for num in nums:
            if num not in cur:
                # cur.append(num) # Choose
                self.helper(nums, cur + [num]) # Explore
                # cur.pop() # Unchoose
        
    def permute(self, nums, cur=[]):       
        self.helper(nums, [])
        return self.ans