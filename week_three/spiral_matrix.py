class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]
        ans = []
        top = 0
        right = len(matrix[0])
        left = -1
        bottom = len(matrix)
        total = len(matrix) * len(matrix[0])
        i=j=0
        while len(ans) < total:
            while i<right and len(ans) < total:
                ans.append(matrix[j][i])
                i+=1
            i-=1
            j+=1
            right-=1
            while j<bottom and len(ans) < total:
                ans.append(matrix[j][i])
                j+=1
            j-=1
            i-=1
            bottom-=1
            while i>left and len(ans) < total:
                ans.append(matrix[j][i])
                i-=1
            i+=1
            j-=1
            left+=1
            while j>top and len(ans) < total:
                ans.append(matrix[j][i])
                j-=1
            j+=1
            i+=1
            top+=1
        return ans

        
