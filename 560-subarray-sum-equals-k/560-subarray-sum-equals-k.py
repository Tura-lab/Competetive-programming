class Solution:
    '''
    tot=1
    [0:1, 3:1, 6:1,3:1 4:1,5:1]
    1 2 3  4  5  6  7 
  0 1 3 6 10 15 21 28
  
    1 -4 12
  0 1 -3 6
    
    
    1 2 3 k=3
  0 1 3 6 sumj-k=sumi
  {0:1, 1:1, 3:1,6:1} 
  abs(k-sumj)=sumi
  tot=1
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)
        counter={}
        count=0
        for i in range(len(pre_sum)):
            val=pre_sum[i] - k
            if val in counter:
                count+=counter[val]
            if pre_sum[i] not in counter:
                counter[pre_sum[i]]=1
            else:
                counter[pre_sum[i]]+=1
        return count