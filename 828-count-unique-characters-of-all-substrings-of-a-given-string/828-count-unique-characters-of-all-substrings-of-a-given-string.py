class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        found = defaultdict(list)
        for i in range(len(s)):
            if not found[s[i]]:
                found[s[i]].append(-1)
            found[s[i]].append(i)
        
        for ls in found.values():
            ls.append(len(s))
            for i in range(1, len(ls)-1):
                ans += ls[i]-ls[i-1]
                ans += ls[i+1]-ls[i]
                ans -= 1
                ans += (ls[i+1]-ls[i]-1)*(ls[i]-ls[i-1]-1)
                
        # print(dict(found))
        return ans
                
                
            
            