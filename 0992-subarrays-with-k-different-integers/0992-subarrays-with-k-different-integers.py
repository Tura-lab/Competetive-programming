class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
      0 1 2 2 2 3
        1,2,1,2,3
        |
              |
        1,2,2,2,3

        '''
        def func(k):
            count = 0
            i, found = 0, {}
            
            for j in range(len(nums)):
                if nums[j] not in found:
                    found[nums[j]] = 1
                else:
                    found[nums[j]] += 1
                
                while len(found) > k:
                    found[nums[i]] -= 1
                    if found[nums[i]] == 0:
                        del found[nums[i]]
                    i += 1
                
                count += j - i + 1
            
            return count
        
        return func(k) - func(k-1)
                    