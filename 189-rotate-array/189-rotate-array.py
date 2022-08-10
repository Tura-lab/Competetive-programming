class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k, n = k%len(nums), len(nums)
        
        def rotate(i,j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        
        # Reverse the first n-k elements
        rotate(0, n-k-1)
        
        # Reverse the rest of the array
        rotate(n-k, n-1)
        
        # Reverse the whole array
        rotate(0,n-1)