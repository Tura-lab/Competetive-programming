class Solution:
    def merge(self, left, right):
        new = []
        i=j=0
        while  i<len(left) and j<len(right):
            if left[i]>right[j]:
                new.append(right[j])
                j+=1
            else:
                new.append(left[i])
                i+=1
        while i<len(left):
            new.append(left[i])
            i+=1
        while j<len(right):
            new.append(right[j])
            j+=1
        return new
            
    def sortArray(self, nums):
        return sorted(nums)
        if len(nums)<=1:
            return nums
        mid   = (len(nums))//2
        left  = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
