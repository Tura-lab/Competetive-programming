class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = [nums[i] for i in range(1, len(nums), 2)]
        even = [nums[i] for i in range(0, len(nums), 2)]
        
        odd.sort(reverse=True)
        even.sort()

        ans = []
        i=0
        while i<len(odd):
            ans.append(even[i])
            ans.append(odd[i])
            i+=1
        if i<len(even):
            ans.append(even[i])
        return ans
        