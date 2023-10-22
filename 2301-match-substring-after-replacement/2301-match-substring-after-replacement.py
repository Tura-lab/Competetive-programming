class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        maps = set()
        
        for key, val in mappings:
            maps.add((key, val))
                
                
        for i in range(len(s) - len(sub) + 1):
            count = 0
            for j in range(len(sub)):
                if not(s[i + j] == sub[j] or (sub[j], s[i + j]) in maps):
                    break
                count += 1
                
            if count == len(sub):
                return True
            
        return False