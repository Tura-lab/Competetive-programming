class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a,b,c = 2,3,5
        a1, b1, c1 = 0,0,0
        nums = [1]
        
        while len(nums) < n:
            val = min(nums[a1]*a, nums[b1]*b, nums[c1]*c)
            nums.append(val)
            
            if val == nums[a1]*a:
                a1 += 1
            if val == nums[b1]*b:
                b1 += 1
            if val == nums[c1]*c:
                c1 += 1
                        
        return nums[-1]