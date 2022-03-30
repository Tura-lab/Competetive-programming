class Solution:
    '''
     AABABBA
     ^
      ^
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        counter = dict()
        i=j=0
        mx=0
        while j<len(s):
            if s[j] in counter:
                counter[s[j]] += 1
            else:
                counter[s[j]] = 1
            
            mx = max(counter[s[j]], mx)
            # print(mx, (j-i+1), 345876534,i)
            if (j-i+1)-mx > k:
                counter[s[i]]-=1
                if counter[s[i]] ==0:
                    del counter[s[i]]
                i+=1
            j+=1
        
        # print(mx, (i,j))
        return j-i
            
            