class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        first_half, second_half = defaultdict(tuple), defaultdict(tuple)
        
        def dfs(i, a, b, nums, d):
            if i == len(nums):
                dif = a - b
                if dif not in d:
                    d[dif] = (a, b)
                    
                else:
                    if a + b > d[dif][0] + d[dif][1]:
                        d[dif] = (a, b)
                        
                return
            
            # let the first take
            dfs(i + 1, a + nums[i], b, nums, d)
            
            # let the second take
            dfs(i + 1, a, b + nums[i], nums, d)
            
            # pass
            dfs(i + 1, a, b, nums, d)
            
        a, b = rods[:len(rods) // 2], rods[len(rods) // 2:]
            
        dfs(0, 0, 0, a, first_half)
        dfs(0, 0, 0, b, second_half)
        
        ans = 0
        for dif, first_pair in first_half.items():
            left, right = first_pair
            
            if -dif in second_half:
                left1, right1 = second_half[-dif]
                ans = max(ans, left + left1)

            
        for dif, first_pair in second_half.items():
            left, right = first_pair
            
            if -dif in first_half:
                left1, right1 = first_half[-dif]
                ans = max(ans, left + left1)
                
                
        return ans