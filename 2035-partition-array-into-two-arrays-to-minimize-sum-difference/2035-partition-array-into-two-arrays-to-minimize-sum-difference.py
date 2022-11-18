class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total, n = sum(nums), len(nums)
        
        first_half  = [[] for _ in range(n//2 + 1)]
        second_half = [[] for _ in range(n//2 + 1)]
        
        
        def dfs(i, count, tot):
            if i == lim:
                ls[count].append(tot)
                return
            
            dfs(i+1, count+1, tot + nums[i])
            dfs(i+1, count, tot)
        
        ls = first_half
        lim = n>>1
        dfs(0, 0, 0)
        
        ls = second_half
        lim = n
        dfs(n>>1, 0, 0)
        
        for arr in first_half:
            arr.sort()

        for arr in second_half:
            arr.sort(reverse=True)
            
        
        smallest = float('inf')
        for i in range(len(first_half)):
            arr1, arr2 = first_half[i], second_half[(n//2) - i]
            
            j,k = 0,0
            
            while j < len(arr1) and k < len(arr2):
                cur = arr1[j] + arr2[k]
                smallest = min(smallest, abs(cur - (total - cur)))
                
                if cur > total - cur:
                    k += 1
                else:
                    j += 1
            
            
            
        return smallest
                        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            