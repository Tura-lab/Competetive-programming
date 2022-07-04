class Solution:
    def candy(self, ratings: List[int]) -> int:
        self.ans = len(ratings)
        sorted_ratings = [(i, ratings[i]) for i in range(len(ratings))]
        sorted_ratings.sort(key=lambda x:x[1])
        
        # print(sorted_ratings)
        candies = [1]*len(ratings)
        
        def fix(i):
            add=0
            if i-1>-1 and i+1<len(ratings):
                add = 0
                if (ratings[i-1]<ratings[i]) and (candies[i-1]>=candies[i]):
                    add += candies[i-1] - candies[i] + 1
                    candies[i] += candies[i-1] - candies[i] + 1
                    
                if (ratings[i+1]<ratings[i]) and (candies[i+1]>=candies[i]):
                    add += candies[i+1] - candies[i] + 1
                    candies[i] += candies[i+1] - candies[i] + 1
                
            elif i==len(ratings)-1:
                # print(899898)
                add = 0
                if (ratings[i-1]<ratings[i]) and (candies[i-1]>=candies[i]):
                    add += candies[i-1] - candies[i] + 1
                    candies[i] += candies[i-1] - candies[i] + 1
            
            elif i==0:
                add = 0
                if (ratings[i+1]<ratings[i]) and (candies[i+1]>=candies[i]):
                    add += candies[i+1] - candies[i] + 1
                    candies[i] += candies[i+1] - candies[i] + 1
                
            self.ans+=add

        
        for i, j in sorted_ratings:
            fix(i)
        
        
        # print([(candies[i], ratings[i]) for i in range(len(ratings))])
        # print(sum(candies))
        return self.ans