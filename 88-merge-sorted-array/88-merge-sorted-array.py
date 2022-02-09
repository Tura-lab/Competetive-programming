class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = []
        i=0
        j=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
        while i<m:
            new.append(nums1[i])
            i+=1
        while j<n:
            new.append(nums2[j])
            j+=1
        for i in range(len(new)):
            nums1[i] = new[i]