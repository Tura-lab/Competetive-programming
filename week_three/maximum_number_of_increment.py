class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        count = {nums[0]:1}
        mx = nums[0]
        for num in nums[1:]:
            if num not in count:
                count[num] = 1
                if num>mx:
                    mx=num
            else:
                n = num + (mx - num + 1)
                ans += (mx - num + 1)
                count[n] = 1
                if n>mx:
                    mx=n
        return ans

    # {1:1,2:1, 3:1, 6:1}
#     1,1,2,2,3,7



