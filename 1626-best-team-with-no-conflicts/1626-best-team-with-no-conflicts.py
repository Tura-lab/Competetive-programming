class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        people = list(zip(ages, scores))
        people.sort()
        
        dp = [score for age, score in people]
        
        
        for i in range(len(people)):
            age, score = people[i]
            for j in range(i):
                if age == people[j][0] or score >= people[j][1]:
                    dp[i] = max(dp[i], score + dp[j])
            
            
        return max(dp)