class Solution:
    '''
    [[3, 2], [4, 3], [4, 4], [2, 5]]
    '''
    def mostPoints(self, questions: List[List[int]]) -> int:
        print(len(questions))
        dp = [-1 for j in range(len(questions))]
        
        def solve(i):
            if i >= len(questions):
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            answer = questions[i][0] + solve(i + questions[i][-1] + 1)
            dont = solve(i+1)
            
            dp[i] = max(answer, dont)
            
            return dp[i]
        return solve(0)