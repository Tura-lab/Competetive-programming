class Solution:
    def quick_sort(self, A, p, r, points):
        if p < r-1:
            q = self.partition(A, p, r, points)
            self.quick_sort(A, p, q, points)
            self.quick_sort(A, q+1, r, points)
        return A
    # The cool step
    def partition(self, A,p,r, points):
        # Take the last element as the pivote
        x = A[r-1]
        i = p-1
        for j in range(p, r):
            if A[j] < x:
                i = i+1
                A[j], A[i] = A[i], A[j]
                points[j], points[i] = points[i], points[j]

        points[i+1], points[r-1] = points[r-1], points[i+1]
        A[i+1], A[r-1] = A[r-1], A[i+1]
        return i+1
    
    def kClosest(self, points, k):
        nums = [(n[0]**2 + n[1]**2) for n in points]
        nums = self.quick_sort(nums,0, len(nums), points)
        return points[:k]
        
