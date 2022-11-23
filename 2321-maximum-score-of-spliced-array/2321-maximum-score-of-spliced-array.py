class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        20  40  20  70  30
        50  20  50  40  20
        '''
        s1, s2 = sum(nums1), sum(nums2)
        # if s2 > s1:
        #     nums1, nums2 = nums2, nums1
            
        curmn = curmx = mn = mx = nums2[0] - nums1[0]
        for i in range(1, len(nums1)):
            curmn += nums2[i] - nums1[i]
            curmx += nums2[i] - nums1[i]
            
            if curmn >= nums2[i] - nums1[i]:
                curmn = nums2[i] - nums1[i]
            if curmx <= nums2[i] - nums1[i]:
                curmx = nums2[i] - nums1[i]
            
            mn = min(mn, curmn)
            mx = max(mx, curmx)
        
        # print(mx, mn, s1, s2)
        return max(s1, s2, s1 + mx, s2 - mn)