class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        reps = {}
        
        i=0
        mapped = set()
        while i<len(s):
            if s[i] not in reps and t[i] in mapped:
                return False
            if s[i] in reps and reps[s[i]] != t[i]:
                return False
            
            mapped.add(t[i])
            reps[s[i]] = t[i]
            i+=1
        return True