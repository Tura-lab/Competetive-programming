class Solution:
    def canConstruct(self, ransomNote: str, megazine: str) -> bool:
        ransomCount = {}
        megazineCount = {}
        
        for i in megazine:
            if i in megazineCount:
                megazineCount[i] +=1
            else:
                megazineCount[i]=1
                
        for i in ransomNote:
            if i in ransomCount:
                ransomCount[i]+=1
            else:
                ransomCount[i]=1
        
        for i,j in ransomCount.items():
            if i not in megazineCount:
                return False
            if megazineCount[i]<j:
                return False
        
        return True