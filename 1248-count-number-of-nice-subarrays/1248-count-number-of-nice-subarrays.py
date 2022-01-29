class Solution:
    '''
    [0:1,1:1,2:1,3:1,]  k=3  c=1
    1 1 2 1 1
    1 1 0 1 1
  0 1 2 2 3 4
    '''
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        pre_sum = [0]
        counter = {}
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
        
        count = 0
        for i in pre_sum:
            if i-k in counter:
                count += counter[i-k]
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        return count