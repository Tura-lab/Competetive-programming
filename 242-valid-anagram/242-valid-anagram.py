class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if not len(s)==len(t):
            return False
        
        goal = {}
        for i in range(len(s)):
            val = s[i]
            if val in goal:
                goal[val] +=1
            else:
                goal[val] =1
        
        d = {}
        for i in range(len(t)):
            val = t[i]
            if val in d:
                d[val]+=1
            else:
                d[val]=1
        return goal == d