class Solution:
    def nextGreaterElement(self, n: int) -> int:
        '''
        123765
        '''
        nums = [int(i) for i in list(str(n))]
        
        s = []
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i+1
                for j in range(i+2, len(nums)):
                    if nums[j] > nums[i] and nums[j] < nums[idx]:
                        idx = j
                
                nums[i], nums[idx] = nums[idx], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                ans = int(''.join([str(i) for i in nums])) 
                return ans if ans < 1<<31 else -1
            
        return -1