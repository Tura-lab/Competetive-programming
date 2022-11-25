class Solution:
    def mergeTriplets(self, nums: List[List[int]], target: List[int]) -> bool:
        possible = []
        a,b,c = target
        A = B = C = False
        
        for i in range(len(nums)):
            if nums[i][0] <= a and nums[i][1] <= b and nums[i][2] <= c:
                A = A or nums[i][0] == a
                B = B or nums[i][1] == b
                C = C or nums[i][2] == c            
            
        return A and B and C