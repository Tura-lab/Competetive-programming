class Solution:
    '''
    1 2 3   k=5
    i
    '''
    def game(self, nums, k, count, index):
        if len(nums)==1:
            return nums[0]
        if count==k:
            count=1
            nums.remove(nums[index])
            if index > len(nums)-1:
                index=0
        else:
            count+=1
            if index == len(nums)-1:
                index=0
            else:
                index+=1
        return self.game(nums, k, count, index)
        
    def findTheWinner(self, n, k):
        nums = list(range(1, n+1))
        return self.game(nums, k, 1, 0)
            