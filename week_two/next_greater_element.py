class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack=[nums2[0]]
        for i in range(1,len(nums2)):
            while stack!=[] and stack[-1]<nums2[i]:
                num = stack.pop()
                d[num] = nums2[i]
            stack.append(nums2[i])

        for num in stack:
            d[num] = -1
        for i in range(len(nums1)):
            nums1[i] = d[nums1[i]]
        return nums1
