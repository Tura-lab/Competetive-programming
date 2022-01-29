class Solution:
    '''
    f=2
    s=1
    0 6  5  2  2  5  1  9  4
  0 6 11 13 15 20 21 30 34
      i     j                
    '''
    def maxSumTwoNoOverlap(self, nums: List[int], f: int, s: int) -> int:
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
        i=0
        j=f
        max=0
        while j<len(pre_sum):
            cur = pre_sum[j]-pre_sum[i]
            k=0 
            l=k+s
            while l<=i:
                if max < pre_sum[l]-pre_sum[k] + cur:
                    max = pre_sum[l]-pre_sum[k] + cur
                k+=1
                l+=1
            k=j 
            l=k+s
            while l<len(pre_sum):
                if max < pre_sum[l]-pre_sum[k] + cur:
                    max = pre_sum[l]-pre_sum[k] + cur
                k+=1
                l+=1
            i+=1
            j+=1
        return max