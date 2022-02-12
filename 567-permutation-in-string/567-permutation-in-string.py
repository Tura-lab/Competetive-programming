class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        # print(len(s1), len(s2))
        goal ={}
        
        for i in range(len(s1)):
            val = s1[i] 
            if val in goal:
                goal[val] += 1
            else:
                goal[val] = 1
                
        d = {}
        for i in range(len(s1)):
            val = s2[i] 
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
        if d==goal:
            return True
        
        j=i+1
        i=1
        while j<len(s2):
            
            d[s2[i-1]]-=1
            if d[s2[i-1]]==0:
                del d[s2[i-1]]
            
            if s2[j] in d:
                d[s2[j]]+=1
            else:
                d[s2[j]]=1
            if d==goal:
                return True
            i+=1
            j+=1
            
        return False
        