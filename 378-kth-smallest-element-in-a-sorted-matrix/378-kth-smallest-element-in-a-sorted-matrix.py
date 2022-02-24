from heapq import heappush, heappop

class Solution:
    '''
    [[1,  5, 9],
     [10,11,13],
     [12,13,15]]
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        i=j=0
        n = len(matrix)
        if k==1:
            return matrix[0][0]
        while len(heap) <k:
            heappush(heap, -matrix[i][j])
            if i==n-1:
                i=0
                j+=1
            else:
                i+=1
            if len(heap) == k:
                break
                    
        while j<len(matrix):
            if -heap[0]>matrix[i][j]:
                heappop(heap)
                heappush(heap, -matrix[i][j])
            if i==n-1:
                i=0
                j+=1
            else:
                i+=1
        return -heap[0]