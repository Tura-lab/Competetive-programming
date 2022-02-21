class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for num in nums:
            if num in ht:
                ht[num]+=1
            else:
                ht[num]=1
            
            if ht[num]>len(nums)//2:
                return num
            