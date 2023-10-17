class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = float('-inf')
        dp = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                dp[j] = (dp[j] + matrix[i][j]) * matrix[i][j]
            
            left = [0] * len(dp)
            right = [len(dp) - 1] * len(dp)

            cur = []
            for j in range(len(dp)):
                while cur and cur[-1][0] > dp[j]:
                    height, idx = cur.pop()
                    right[idx] = j - 1
                cur.append((dp[j], j))
            
            cur = []
            for j in range(len(dp) - 1, -1, -1):
                while cur and cur[-1][0] > dp[j]:
                    height, idx = cur.pop()
                    left[idx] = j + 1
                cur.append((dp[j], j))
            
            # print(dp)
            # print(left)
            # print(right)
            
            for j in range(len(dp)):
                ans = max(ans, dp[j] * (right[j] - left[j] + 1))
            
        return ans