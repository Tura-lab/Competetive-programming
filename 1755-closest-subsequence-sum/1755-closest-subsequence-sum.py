class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        l1 = []
        l2 = []
        def all_subsets(i, end, _sum,arr):
            if i == end:
                arr.append(_sum)
                return
            
            all_subsets(i+1, end, _sum+nums[i], arr)
            all_subsets(i+1, end, _sum, arr)
        
        end = len(nums)//2
        
        all_subsets(0, end, 0,l1)
        all_subsets(end, len(nums), 0, l2)
        
        l1.sort()
        l2.sort(reverse=True)
        
        i=j=0
        ans = float('inf')
        while i<len(l1) and j<len(l2):
            cur = l1[i]+l2[j]
            if cur > goal:
                j+=1 
            elif cur<goal:
                i+=1
            else:
                return 0
            
            ans = min(ans,abs(cur-goal))
            
            
        return ans
            
            
        