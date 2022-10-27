class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dp = [[False] * numCourses for _ in range(numCourses)]
        
        for a,b in prerequisites:
            dp[a][b] = True
        
        for k in range(numCourses):
            for j in range(numCourses):
                for i in range(numCourses):
                    if i==j or j==k or i == k:continue
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
        
        return [dp[a][b] for a,b in queries]
            