class Solution:
    def __init__(self):
        self.cache = {}
        
    def ans(self,nums,i):
        if i==len(nums)-3:
            return nums[-3] + nums[-1]
        elif i==len(nums)-2:
            return nums[-2]
        elif i==len(nums)-1:
            return nums[-1]
        if i+2 in self.cache:
            # print('in')
            first = self.cache[i+2] + nums[i]
        else:
            self.cache[i+2] = self.ans(nums, i+2)
            first = self.cache[i+2] + nums[i]
        if i+3 in self.cache:
            # print('in')
            second = self.cache[i+3] + nums[i]
        else:
            self.cache[i+3] = self.ans(nums, i+3)
            second = self.cache[i+3] + nums[i]
            
        return max(first, second)
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        first = self.ans(nums,0)
        second = self.ans(nums,1)
        return max(first,second)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # i=0
        # j=1
        # s1 = nums[i]
        # s2 = nums[j]
        # while i<len(nums)-2:
        #     if i==len(nums)-3:
        #         print(nums[-1],end=',')
        #         s1+=nums[-1]
        #         break
        #     if nums[i+3] > nums[i+2]:
        #         s1+=nums[i+3]
        #         print(nums[i+3], end=',')
        #         i=i+3
        #     else:
        #         print(nums[i+2], end=',')
        #         s1+=nums[i+2]
        #         i=i+2
        # print()
        # while j<len(nums)-2:
        #     if j==len(nums)-3:
        #         print(nums[-1],end=',')
        #         s2+=nums[-1]
        #         break
        #     if nums[j+3] > nums[j+2]:
        #         print(nums[j+3], end=',')
        #         s2+=nums[j+3]
        #         j=j+3
        #     else:
        #         print(nums[j+2], end=',')
        #         s2+=nums[j+2]
        #         j=j+2
        # print()
        # return max(s1,s2)