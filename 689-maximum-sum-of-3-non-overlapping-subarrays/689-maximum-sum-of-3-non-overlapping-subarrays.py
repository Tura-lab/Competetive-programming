from collections import deque

class Solution:
    '''
      1 2 1 2  6  7  5  1 
    0 1 3 4 6 12 19 24 25 
    0 1 2 3 4  5  6  7  8
(0, 2, 3), (0, 2, 3), (0, 2, 3), (3, 5, 8), (4, 6, 13), (4, 6, 13), (4, 6, 13)
(4, 6, 13), (4, 6, 13), (4, 6, 13), (4, 6, 13), (4, 6, 13), (5, 7, 12), (6, 8, 6)
    '''
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(num + pre_sum[-1])
        
        right = deque()
        left = []
        
        yet = 0
        idx = (0,0)
        j=k
        while j <= len(pre_sum)-(2*k+1):
            i = j-k
            if pre_sum[j]-pre_sum[i] > yet:
                yet = pre_sum[j]-pre_sum[i]
                idx = (i,j,yet)
            left.append(idx)
            j+=1
            
        yet = 0
        idx = (0,0)
        j=len(pre_sum)-1
        while j >= k:
            i = j-k
            if pre_sum[j]-pre_sum[i] >= yet:
                yet = pre_sum[j]-pre_sum[i]
                idx = (i,j,yet)
            right.appendleft(idx)
            if i == 2*k:
                break
            j-=1
            
        # print(left)
        # print(right)

        ans = 0
        idx = ()
        i=k
        l=0
        while l < len(left):
            j=i+k
            cur = left[l][-1] + right[l][-1] + pre_sum[j]-pre_sum[i]
            if cur > ans:
                ans = cur
                idx = (left[l][0], i, right[l][0])
            l+=1
            i+=1
        # print(ans)
        return idx
            
            
            
            
            
            
            