from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k in nums:
            return 1
        elif len(nums)==1:
            return -1
        sums_arr = [0] * (len(nums)+1)
        for i in range(1,len(sums_arr)):
            sums_arr[i] = sums_arr[i-1] + nums[i-1]
        smallest = len(nums)
        j=1
        found=False
        stack = deque()
        stack.append(0)
        while j<len(sums_arr):
            while len(stack)>0 and sums_arr[stack[-1]]-sums_arr[stack[0]] >= sums_arr[j]-sums_arr[stack[0]]:
                stack.pop()
            stack.append(j)
            while len(stack)>0 and sums_arr[stack[-1]]-sums_arr[stack[0]]>=k:
                found=True
                if stack[-1]-stack[0] < smallest:
                    smallest = stack[-1]-stack[0]
                stack.popleft()       
            j+=1
        return smallest if found else -1
