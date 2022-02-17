class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            item = s[i]
            if item in d:
                d[item][0]+=1
            else:
                d[item]=[1,i]
        
        
        for i,j in d.items():
            if j[0]==1:
                return j[1]
            
        return -1