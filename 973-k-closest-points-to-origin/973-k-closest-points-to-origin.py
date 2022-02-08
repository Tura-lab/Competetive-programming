class Solution:
    
    def kClosest(self, points, k):
        nums = [(n[0]**2 + n[1]**2, n) for n in points]
        nums.sort(key= lambda item: item[0])
        return [n[-1] for n in nums[:k]]
        