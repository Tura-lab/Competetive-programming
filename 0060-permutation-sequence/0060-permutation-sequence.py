class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        1,2,3
        
        '''
        
        factorials = [1]
        for i in range(1, n+1):
            factorials.append(factorials[-1] * i)
        
        nums = [i for i in range(1, n+1)]
        ans = []
        
        while len(ans) < n:
            i = 0
            count = 0
            while count + factorials[(len(nums) - 1)] < k:
                i += 1
                count += factorials[(len(nums) - 1)]
            
            ans.append(str(nums[i]))
            nums.remove(nums[i])
            
            k -= count
            
        return ''.join(ans) 
            