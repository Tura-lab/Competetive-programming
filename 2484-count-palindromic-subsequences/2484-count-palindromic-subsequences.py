class Solution:
    def countPalindromes(self, nums: str) -> int:
        
        n, mod = len(nums), 10 ** 9 + 7
        
        pair_counts_left = [[[0] * 10 for _ in range(10)] for __ in range(n)]
        
        cur_counts = [0] * 10
        for i in range(n):            
            if i > 0: 
                for k in range(10):
                    for l in range(10):
                        pair_counts_left[i][k][l] = pair_counts_left[i-1][k][l]
            
            for num in range(10):
                pair_counts_left[i][int(nums[i])][num] += cur_counts[num]
            
            cur_counts[int(nums[i])] += 1
            
        
        pair_counts_right = [[[0] * 10 for _ in range(10)] for __ in range(n)]
        
        cur_counts = [0] * 10
        for i in range(n-1, -1, -1):            
            if i < n-1: 
                for k in range(10):
                    for l in range(10):
                        pair_counts_right[i][k][l] = pair_counts_right[i+1][k][l]
            
            for num in range(10):
                pair_counts_right[i][int(nums[i])][num] += cur_counts[num] 
            
            cur_counts[int(nums[i])] += 1
            
        count = 0
        for i in range(2, n-2):
            prev, nxt = pair_counts_left[i-1], pair_counts_right[i+1]
            
            for num1 in range(10):
                for num2 in range(10):
                    # print(i, (num1, num2), (prev[num1][num2], nxt[num1][num2]))
                    count += prev[num1][num2] * nxt[num1][num2]
                    count %= mod
                    
        return count 